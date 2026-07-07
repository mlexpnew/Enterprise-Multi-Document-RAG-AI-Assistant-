from __future__ import annotations

from pathlib import Path
from typing import List

import streamlit as st

from config.settings import DATA_FOLDER
from ingestion.ingest import DocumentIngestion
from utils.logger import log


class DocumentUploader:
    """
    Enterprise Document Upload Manager

    Features
    --------
    • Multi PDF Upload
    • Progress Bar
    • Duplicate-safe Indexing
    • Dashboard Statistics
    • Error Handling
    """

    def __init__(self):

        self.pipeline = DocumentIngestion()

        DATA_FOLDER.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_file(self, uploaded_file) -> Path:

        destination = DATA_FOLDER / uploaded_file.name

        with open(destination, "wb") as file:

            file.write(uploaded_file.getbuffer())

        return destination

    def process(self, uploaded_files: List):

        total_files = len(uploaded_files)

        progress = st.progress(0)

        status = st.empty()

        total_chunks = 0

        indexed_files = 0

        failed_files = []

        for index, uploaded_file in enumerate(uploaded_files):

            try:

                status.info(
                    f"Indexing {uploaded_file.name}"
                )

                saved_path = self.save_file(
                    uploaded_file
                )

                chunks = self.pipeline.ingest(
                    str(saved_path)
                )

                total_chunks += chunks

                indexed_files += 1

                progress.progress(
                    (index + 1) / total_files
                )

            except Exception as exc:

                failed_files.append(
                    uploaded_file.name
                )

                log.exception(exc)

        progress.empty()

        status.empty()

        st.session_state["document_count"] = (
            indexed_files
        )

        st.session_state["chunk_count"] = (
            total_chunks
        )

        if indexed_files:

            st.success(
                f"Successfully indexed "
                f"{indexed_files} document(s)."
            )

        st.info(
            f"Total Chunks Indexed : {total_chunks}"
        )

        if failed_files:

            st.error(
                "Failed Documents"
            )

            for name in failed_files:

                st.write(f"• {name}")


def uploader():

    st.subheader("📄 Document Upload")

    uploaded_files = st.file_uploader(
        label="Upload PDF Documents",
        type=["pdf"],
        accept_multiple_files=True,
    )

    if not uploaded_files:

        return

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Selected Files",
            len(uploaded_files),
        )

    with col2:

        total_size = sum(
            file.size
            for file in uploaded_files
        ) / (1024 * 1024)

        st.metric(
            "Upload Size",
            f"{total_size:.2f} MB",
        )

    if st.button(
        "🚀 Index Documents",
        use_container_width=True,
    ):

        manager = DocumentUploader()

        manager.process(uploaded_files)

    st.divider()

    st.caption(
        "Supported Format : PDF"
    )