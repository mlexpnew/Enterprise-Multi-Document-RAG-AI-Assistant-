from __future__ import annotations

from pathlib import Path
from typing import List

from embeddings.embedding_service import EmbeddingService
from ingestion.chunker import ChunkService
from ingestion.metadata import create_metadata
from ingestion.pdf_loader import PDFLoader
from utils.helpers import generate_document_id
from utils.logger import log
from vectorstore.chroma_manager import ChromaManager


class DocumentIngestion:
    """
    Enterprise Document Ingestion Pipeline

    Pipeline
    --------
    PDF
      ↓
    Text Extraction
      ↓
    Chunking
      ↓
    Embedding Generation
      ↓
    ChromaDB Storage
    """

    def __init__(self):

        self.chunker = ChunkService()
        self.embedding_service = EmbeddingService()
        self.vector_store = ChromaManager()

    def ingest_pdf(self, file_path: str) -> int:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(path)

        log.info("Loading document: {}", path.name)

        log.info("STEP 1 : Loading PDF")

        pages = PDFLoader.load(str(path))

        log.info("STEP 2 : PDF Loaded")

        if not pages:
            log.warning("No readable text found.")
            return 0

        log.info("STEP 3 : Chunking")

        chunks = self.chunker.split(pages)

        log.info("STEP 4 : Chunking Completed")

        if not chunks:
            log.warning("No chunks generated.")
            return 0

        texts: List[str] = [
            chunk["text"]
            for chunk in chunks
        ]

        log.info("STEP 5 : Creating Embeddings")
        log.info("Total Chunks: {}", len(texts))

        embeddings = self.embedding_service.embed_batch(
            texts
        )

        log.info("STEP 6 : Embeddings Ready")

        file_metadata = create_metadata(
            str(path)
        )

        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:

            ids.append(
                generate_document_id(
                    chunk["text"]
                )
            )

            documents.append(
                chunk["text"]
            )

            metadata = dict(file_metadata)

            metadata["page"] = chunk["page"]
            metadata["chunk_size"] = len(
                chunk["text"]
            )

            metadatas.append(metadata)

        log.info("STEP 7 : Saving into Chroma")

        inserted = self.vector_store.add_documents(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        log.info("STEP 8 : Chroma Saved")

        log.info(
            "{} chunks indexed from {}",
            inserted,
            path.name,
        )

        return inserted

    def ingest(self, file_path: str) -> int:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return self.ingest_pdf(file_path)

        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    def collection_size(self) -> int:

        return self.vector_store.count()