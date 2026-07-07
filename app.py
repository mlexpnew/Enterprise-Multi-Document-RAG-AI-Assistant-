import streamlit as st
from ui.chat import display_sources
from services.rag_pipeline import RAGPipeline
from config.settings import (
    APP_TITLE,
    PAGE_ICON,
    PAGE_LAYOUT,
)

from ui.sidebar import sidebar
from ui.dashboard import dashboard
from ui.chat import (
    display_chat,
    user_input,
    add_message,
)
from ui.uploader import uploader
from api.client import APIClient


st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=PAGE_LAYOUT,
)

sidebar()

st.title(APP_TITLE)

dashboard()

uploader()

display_chat()

question = user_input()

if question:

    add_message("user", question)

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):

            try:

                result = APIClient.ask(
                    question=question,
                    top_k=st.session_state.get("top_k", 5),
                )

                response = result["answer"]

                st.markdown(response)

                st.success(
                    f"Confidence : {result['confidence']}%"
                )

                if result["citations"]:

                    st.divider()

                    st.subheader("Sources")

                    for source in result["citations"]:

                        st.write(
                            f"📄 {source['file']} | Page {source['page']}"
                        )

                add_message(
                    "assistant",
                    response,
                )

            except Exception as e:

                st.error(
                    f"Error : {str(e)}"
                )

                raise