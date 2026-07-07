from __future__ import annotations

from typing import Dict, List

import streamlit as st


class ChatMemory:
    """
    Enterprise Conversation Memory

    Features
    --------
    ✓ Persistent chat history
    ✓ Conversation context
    ✓ Session based memory
    ✓ Clear conversation
    """

    SESSION_KEY = "chat_history"

    @classmethod
    def initialize(cls):

        if cls.SESSION_KEY not in st.session_state:

            st.session_state[cls.SESSION_KEY] = []

    @classmethod
    def add(
        cls,
        role: str,
        message: str,
    ):

        cls.initialize()

        st.session_state[cls.SESSION_KEY].append(
            {
                "role": role,
                "content": message,
            }
        )

    @classmethod
    def history(cls) -> List[Dict]:

        cls.initialize()

        return st.session_state[cls.SESSION_KEY]

    @classmethod
    def clear(cls):

        st.session_state[cls.SESSION_KEY] = []

    @classmethod
    def context(
        cls,
        turns: int = 5,
    ) -> str:

        cls.initialize()

        history = st.session_state[cls.SESSION_KEY][-turns:]

        conversation = []

        for item in history:

            conversation.append(
                f"{item['role'].upper()}: {item['content']}"
            )

        return "\n".join(conversation)