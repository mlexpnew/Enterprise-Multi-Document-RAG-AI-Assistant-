from __future__ import annotations

from typing import Dict, List

import streamlit as st


class SourceViewer:
    """
    Enterprise Source Viewer

    Features
    --------
    ✓ Expandable Sources
    ✓ Similarity Score
    ✓ Page Number
    ✓ File Name
    ✓ Chunk Preview
    ✓ Copy Source Text
    """

    @staticmethod
    def show(
        citations: List[Dict],
    ):

        if not citations:

            st.info("No source documents available.")

            return

        st.divider()

        st.subheader("📚 Source References")

        for index, source in enumerate(citations, start=1):

            filename = source.get(
                "file",
                "Unknown Document",
            )

            page = source.get(
                "page",
                "-",
            )

            similarity = source.get(
                "score",
                None,
            )

            preview = source.get(
                "text",
                "",
            )

            with st.expander(
                f"📄 {filename}  |  Page {page}"
            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Page",
                        page,
                    )

                with col2:

                    if similarity is not None:

                        st.metric(
                            "Similarity",
                            f"{similarity*100:.2f}%",
                        )

                if preview:

                    st.markdown(
                        "### Preview"
                    )

                    st.code(
                        preview,
                        language="text",
                    )

                    st.download_button(
                        label="📥 Download Chunk",
                        data=preview,
                        file_name=f"chunk_{index}.txt",
                        mime="text/plain",
                        use_container_width=True,
                    )

                else:

                    st.info(
                        "Preview unavailable."
                    )

    @staticmethod
    def compact(
        citations: List[Dict],
    ):

        if not citations:

            return

        st.caption("Retrieved Sources")

        for source in citations:

            filename = source.get(
                "file",
                "Unknown",
            )

            page = source.get(
                "page",
                "-",
            )

            similarity = source.get(
                "score",
                None,
            )

            if similarity is not None:

                st.write(
                    f"• {filename} | Page {page} | {similarity*100:.1f}%"
                )

            else:

                st.write(
                    f"• {filename} | Page {page}"
                )