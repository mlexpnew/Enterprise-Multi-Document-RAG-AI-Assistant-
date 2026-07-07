import streamlit as st

def sidebar():

    with st.sidebar:

        st.title("Enterprise RAG")

        st.caption("AI Engineer Portfolio Project")

        st.divider()

        st.header("Settings")

        top_k = st.slider(
            "Top K Retrieval",
            1,
            10,
            5
        )

        st.session_state["top_k"] = top_k

        st.divider()

        st.header("Statistics")

        st.write(
            "Documents:",
            st.session_state.get("document_count", 0)
        )

        st.write(
            "Chunks:",
            st.session_state.get("chunk_count", 0)
        )

        st.divider()

        if st.button("Clear Chat"):

            st.session_state.messages = []

            st.rerun()