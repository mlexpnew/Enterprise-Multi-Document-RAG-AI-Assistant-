from __future__ import annotations
import os

import requests


class APIClient:

    import os

    BASE_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000",
)

    @classmethod
    def ask(
        cls,
        question: str,
        top_k: int = 5,
    ):

        response = requests.post(
            f"{cls.BASE_URL}/chat/",
            json={
                "question": question,
                "top_k": top_k,
            },
            timeout=120,
        )

        response.raise_for_status()

        return response.json()

    @classmethod
    def health(cls):

        response = requests.get(
            f"{cls.BASE_URL}/health/"
        )

        return response.json()

    @classmethod
    def document_stats(cls):

        response = requests.get(
            f"{cls.BASE_URL}/documents/stats"
        )

        return response.json()