from __future__ import annotations

import streamlit as st

from feedback.feedback_storage import FeedbackStorage


class FeedbackManager:
    """
    Enterprise Feedback Manager

    Features
    --------
    ✓ Thumbs Up
    ✓ Thumbs Down
    ✓ Optional Comment
    ✓ CSV Storage
    """

    @staticmethod
    def collect(
        question: str,
        answer: str,
    ):

        st.divider()

        st.subheader("📝 Feedback")

        col1, col2 = st.columns(2)

        rating = None

        with col1:

            if st.button(
                "👍 Helpful",
                use_container_width=True,
            ):
                rating = "Positive"

        with col2:

            if st.button(
                "👎 Not Helpful",
                use_container_width=True,
            ):
                rating = "Negative"

        comment = st.text_area(
            "Additional Comments (Optional)",
            placeholder="Tell us how we can improve...",
        )

        if rating:

            FeedbackStorage.save(
                question=question,
                answer=answer,
                rating=rating,
                comment=comment,
            )

            st.success(
                "Thank you! Your feedback has been recorded."
            )