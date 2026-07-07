from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd

from config.settings import DATA_FOLDER
from vectorstore.chroma_manager import ChromaManager


class DocumentManager:
    """
    Enterprise Document Manager

    Features
    --------
    ✓ List Documents
    ✓ Document Statistics
    ✓ File Size
    ✓ Upload Time
    ✓ Delete Document
    ✓ Search Documents
    ✓ Collection Summary
    """

    def __init__(self):

        self.data_folder = DATA_FOLDER

        self.vector_store = ChromaManager()

        self.data_folder.mkdir(
            parents=True,
            exist_ok=True,
        )

    def list_documents(self) -> List[Path]:

        return sorted(
            self.data_folder.glob("*.pdf")
        )

    def total_documents(self) -> int:

        return len(
            self.list_documents()
        )

    def document_exists(
        self,
        filename: str,
    ) -> bool:

        return (
            self.data_folder / filename
        ).exists()

    def file_size(
        self,
        file: Path,
    ) -> float:

        return round(
            file.stat().st_size / (1024 * 1024),
            2,
        )

    def upload_time(
        self,
        file: Path,
    ) -> str:

        timestamp = datetime.fromtimestamp(
            file.stat().st_mtime
        )

        return timestamp.strftime(
            "%d-%m-%Y %H:%M"
        )

    def summary(self) -> List[Dict]:

        documents = []

        for file in self.list_documents():

            documents.append(
                {
                    "Filename": file.name,
                    "Size (MB)": self.file_size(file),
                    "Uploaded": self.upload_time(file),
                }
            )

        return documents

    def dataframe(self) -> pd.DataFrame:

        return pd.DataFrame(
            self.summary()
        )

    def search(
        self,
        keyword: str,
    ) -> List[Dict]:

        keyword = keyword.lower()

        results = []

        for item in self.summary():

            if keyword in item[
                "Filename"
            ].lower():

                results.append(item)

        return results

    def delete(
        self,
        filename: str,
    ) -> bool:

        file = (
            self.data_folder / filename
        )

        if not file.exists():

            return False

        file.unlink()

        return True

    def storage_usage(self) -> float:

        total = 0

        for file in self.list_documents():

            total += file.stat().st_size

        return round(
            total / (1024 * 1024),
            2,
        )

    def collection_summary(self) -> Dict:

        return {

            "Total Documents":
                self.total_documents(),

            "Indexed Chunks":
                self.vector_store.count(),

            "Storage (MB)":
                self.storage_usage(),
        }