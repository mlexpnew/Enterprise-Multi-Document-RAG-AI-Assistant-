from __future__ import annotations

from typing import Dict, List, Tuple

from utils.logger import log


class ContextBuilder:
    """
    Enterprise Context Builder

    Converts retrieved chunks into:

    1. LLM Context
    2. Citations
    """

    @staticmethod
    def build(
        retrieved_chunks: List[Dict],
    ) -> Tuple[str, List[Dict]]:

        if not retrieved_chunks:

            log.warning("No retrieved context.")

            return "", []

        context_parts = []

        citations = []

        for index, chunk in enumerate(retrieved_chunks, start=1):

            metadata = chunk.get("metadata", {})

            filename = metadata.get(
                "filename",
                metadata.get(
                    "source",
                    "Unknown Document",
                ),
            )

            page = metadata.get("page", "-")

            score = round(
                float(chunk.get("score", 0)),
                4,
            )

            context_parts.append(
                f"""
========================
DOCUMENT {index}

File : {filename}
Page : {page}

Content:
{chunk['text']}
========================
"""
            )

            citations.append(
                {
                    "rank": index,
                    "file": filename,
                    "page": page,
                    "score": score,
                }
            )

        context = "\n".join(context_parts)

        log.info(
            "Context built using {} chunks.",
            len(retrieved_chunks),
        )

        return context, citations