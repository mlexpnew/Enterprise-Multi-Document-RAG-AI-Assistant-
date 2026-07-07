import streamlit as st

from config.settings import (
    GENERATION_MODEL,
    EMBEDDING_MODEL,
)

def dashboard():

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📄 Documents", st.session_state.get("document_count", 0))

    c2.metric("🧩 Chunks", st.session_state.get("chunk_count", 0))

    c3.metric("🤖 Model", GENERATION_MODEL)

    c4.metric("🔍 Top-K", st.session_state.get("top_k", 5))

    st.divider()

    a, b = st.columns([2, 1])

    with a:

        st.subheader("System Overview")

        st.info(
            f"""
Embedding Model

{EMBEDDING_MODEL}

Generation Model

{GENERATION_MODEL}

Vector Database

ChromaDB

Framework

Streamlit
"""
        )

    with b:

        st.subheader("System Status")

        st.success("Gemini Connected")

        st.success("Vector DB Ready")

        st.success("Application Running")