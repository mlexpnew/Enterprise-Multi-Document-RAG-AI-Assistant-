from __future__ import annotations

from pathlib import Path
from typing import Dict

from config.settings import DATA_FOLDER
from vectorstore.chroma_manager import ChromaManager


class DocumentStatistics:
    """
    Enterprise Document Analytics

    Features
    --------
    ✓ Uploaded PDFs
    ✓ Chroma Collection Size
    ✓ Storage Usage
    ✓ Average Chunks
    """

    def __init__(self):

        self.vector_store = ChromaManager()

    def total_documents(self) -> int:

        return len(
            list(
                DATA_FOLDER.glob("*.pdf")
            )
        )

    def total_chunks(self) -> int:

        return self.vector_store.count()

    def storage_size(self) -> float:

        total = 0

        for file in DATA_FOLDER.glob("*"):

            if file.is_file():

                total += file.stat().st_size

        return round(
            total / (1024 * 1024),
            2,
        )

    def average_chunks(self) -> float:

        docs = self.total_documents()

        if docs == 0:

            return 0

        return round(
            self.total_chunks() / docs,
            2,
        )

    def summary(self) -> Dict:

        return {

            "Total Documents": self.total_documents(),

            "Indexed Chunks": self.total_chunks(),

            "Average Chunks / Document":
                self.average_chunks(),

            "Storage (MB)":
                self.storage_size(),
        }