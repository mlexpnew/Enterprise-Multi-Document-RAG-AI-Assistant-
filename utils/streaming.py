from __future__ import annotations

import time
from typing import Generator

import streamlit as st


class StreamResponse:
    """
    Enterprise Streaming Response

    Features
    --------
    ✓ ChatGPT typing effect
    ✓ Markdown support
    ✓ Cursor animation
    ✓ Adjustable speed
    """

    @staticmethod
    def stream(
        text: str,
        delay: float = 0.015,
    ) -> Generator[str, None, None]:

        words = text.split()

        current = ""

        for word in words:

            current += word + " "

            yield current + "▌"

            time.sleep(delay)

        yield current

    @staticmethod
    def display(
        text: str,
        delay: float = 0.015,
    ) -> str:

        placeholder = st.empty()

        final_text = ""

        for chunk in StreamResponse.stream(
            text,
            delay,
        ):

            placeholder.markdown(chunk)

            final_text = chunk.replace(
                "▌",
                "",
            )

        placeholder.markdown(final_text)

        return final_text