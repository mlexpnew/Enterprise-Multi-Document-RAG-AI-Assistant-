from __future__ import annotations

import hashlib
from typing import Dict


class QueryCache:
    """
    Enterprise Query Cache

    Prevents repeated LLM calls.
    """

    def __init__(self):

        self.cache: Dict = {}

    @staticmethod
    def key(question: str) -> str:

        return hashlib.md5(
            question.lower().encode()
        ).hexdigest()

    def exists(
        self,
        question: str,
    ) -> bool:

        return self.key(question) in self.cache

    def get(
        self,
        question: str,
    ):

        return self.cache.get(
            self.key(question)
        )

    def save(
        self,
        question: str,
        answer,
    ):

        self.cache[
            self.key(question)
        ] = answer

    def clear(self):

        self.cache.clear()

    def size(self):

        return len(self.cache)