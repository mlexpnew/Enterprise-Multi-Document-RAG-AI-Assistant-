from __future__ import annotations

import streamlit as st


def initialize_chat():

    if "messages" not in st.session_state:

        st.session_state.messages = []


def add_message(
    role: str,
    content: str,
):

    initialize_chat()

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def display_chat():

    initialize_chat()

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])


def user_input():

    return st.chat_input(
        "Ask anything about your uploaded documents..."
    )


def display_sources(
    citations,
):

    if not citations:

        return

    st.divider()

    st.subheader("📚 Retrieved Sources")

    for source in citations:

        similarity = source.get(
            "score",
            0,
        )

        with st.expander(
            f"📄 {source['file']} | Page {source['page']}"
        ):

            st.metric(
                "Similarity",
                f"{similarity*100:.2f}%"
            )

            if "text" in source:

                st.write(source["text"])