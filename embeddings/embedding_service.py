from __future__ import annotations

import time
from typing import List

import google.generativeai as genai

from config.settings import (
    GOOGLE_API_KEY,
    EMBEDDING_MODEL,
)
from utils.logger import log


class EmbeddingService:

    _configured = False

    def __init__(self):

        if not self.__class__._configured:

            if not GOOGLE_API_KEY:
                raise ValueError("GOOGLE_API_KEY not found.")

            genai.configure(api_key=GOOGLE_API_KEY)

            self.__class__._configured = True

            log.info("Gemini Embedding Service initialized.")

    def embed(self, text: str) -> List[float]:

        response = genai.embed_content(
            model=EMBEDDING_MODEL,
            content=text,
            task_type="retrieval_document",
        )

        return response["embedding"]

    def embed_batch(
        self,
        texts: List[str],
    ) -> List[List[float]]:

        embeddings = []

        total = len(texts)

        log.info("Creating {} embeddings...", total)

        for index, text in enumerate(texts, start=1):

            retries = 3

            while retries > 0:

                try:

                    response = genai.embed_content(
                        model=EMBEDDING_MODEL,
                        content=text,
                        task_type="retrieval_document",
                    )

                    embeddings.append(response["embedding"])

                    log.info(
                        "Embedded {}/{}",
                        index,
                        total,
                    )

                    # Small delay to reduce rate limiting
                    time.sleep(0.25)

                    break

                except Exception as e:

                    retries -= 1

                    log.warning(
                        "Embedding failed for chunk {}. Retries left: {}",
                        index,
                        retries,
                    )

                    if retries == 0:
                        raise RuntimeError(
                            f"Embedding failed for chunk {index}: {e}"
                        )

                    time.sleep(2)

        log.info("Finished generating embeddings.")

        return embeddings