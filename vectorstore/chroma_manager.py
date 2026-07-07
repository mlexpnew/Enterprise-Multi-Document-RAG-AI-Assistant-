from __future__ import annotations

from typing import Any, Dict, List

import chromadb

from config.settings import CHROMA_DB
from utils.logger import log


class ChromaManager:
    """
    Enterprise ChromaDB Manager

    Features
    --------
    ✓ Persistent Storage
    ✓ Duplicate Detection
    ✓ Similarity Search
    ✓ Collection Reset
    ✓ Collection Statistics
    """

    COLLECTION_NAME = "enterprise_rag"

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB)
        )

        self.collection = self.client.get_or_create_collection(
            name=self.COLLECTION_NAME,
            metadata={
                "hnsw:space": "cosine"
            },
        )

        log.info(
            "Connected to Chroma Collection: {}",
            self.COLLECTION_NAME,
        )

    def count(self) -> int:

        return self.collection.count()

    def add_documents(
        self,
        ids: List[str],
        documents: List[str],
        embeddings: List[List[float]],
        metadatas: List[Dict[str, Any]],
    ) -> int:

        if not documents:
            return 0

        existing = self.collection.get(ids=ids)

        existing_ids = set(existing.get("ids", []))

        new_ids = []
        new_documents = []
        new_embeddings = []
        new_metadatas = []

        for index, doc_id in enumerate(ids):

            if doc_id not in existing_ids:

                new_ids.append(doc_id)

                new_documents.append(
                    documents[index]
                )

                new_embeddings.append(
                    embeddings[index]
                )

                new_metadatas.append(
                    metadatas[index]
                )

        if not new_documents:

            log.info(
                "No new documents to insert."
            )

            return 0

        self.collection.add(
            ids=new_ids,
            documents=new_documents,
            embeddings=new_embeddings,
            metadatas=new_metadatas,
        )

        log.info(
            "{} chunks indexed.",
            len(new_documents),
        )

        return len(new_documents)

    def search(
        self,
        embedding: List[float],
        top_k: int = 5,
    ) -> Dict:

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances",
            ],
        )

    def similarity_search(
        self,
        embedding: List[float],
        top_k: int = 5,
    ) -> Dict:

        return self.search(
            embedding=embedding,
            top_k=top_k,
        )

    def delete_collection(self):

        try:

            self.client.delete_collection(
                self.COLLECTION_NAME
            )

        except Exception:

            pass

        self.collection = (
            self.client.get_or_create_collection(
                name=self.COLLECTION_NAME,
                metadata={
                    "hnsw:space": "cosine"
                },
            )
        )

        log.info(
            "Collection reset completed."
        )

    def get_collection(self):

        return self.collection