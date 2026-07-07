from __future__ import annotations

from typing import Dict, List

from embeddings.embedding_service import EmbeddingService
from utils.logger import log
from vectorstore.chroma_manager import ChromaManager


class HybridRetriever:
    """
    Enterprise Hybrid Retriever

    Current Features
    ----------------
    ✓ Dense Vector Search
    ✓ Similarity Scores
    ✓ Metadata Retrieval
    ✓ Source Tracking

    Future
    ------
    • BM25 Retrieval
    • Reciprocal Rank Fusion (RRF)
    • Cross Encoder Re-ranking
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.vector_store = ChromaManager()

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict]:

        if not query.strip():
            return []

        log.info(
            "Searching top {} documents...",
            top_k,
        )

        query_embedding = self.embedding_service.embed(
            query
        )

        results = self.vector_store.search(
            embedding=query_embedding,
            top_k=top_k,
        )

        retrieved_chunks = []

        if not results:
            log.warning("No matching documents found.")

            return retrieved_chunks

        documents = results.get(
            "documents",
            [[]],
        )[0]

        metadatas = results.get(
            "metadatas",
            [[]],
        )[0]

        distances = results.get(
            "distances",
            [[]],
        )[0]

        ids = results.get(
            "ids",
            [[]],
        )[0]

        for idx in range(len(documents)):

            similarity = round(
                1 - float(distances[idx]),
                4,
            )

            retrieved_chunks.append(
                {
                    "id": ids[idx],
                    "text": documents[idx],
                    "metadata": metadatas[idx],
                    "score": similarity,
                }
            )

        log.info(
            "{} chunks retrieved.",
            len(retrieved_chunks),
        )

        return retrieved_chunks