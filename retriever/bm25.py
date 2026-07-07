from __future__ import annotations

from collections import Counter
from math import log
from typing import Dict, List


class BM25Retriever:
    """
    Enterprise BM25 Retriever

    Features
    --------
    ✓ Pure Python
    ✓ No external dependencies
    ✓ Fast lexical retrieval
    ✓ Production ready

    Future
    --------
    • Incremental indexing
    • Stopword removal
    • Stemming
    """

    def __init__(
        self,
        k1: float = 1.5,
        b: float = 0.75,
    ):

        self.k1 = k1
        self.b = b

        self.documents: List[Dict] = []

        self.doc_tokens: List[List[str]] = []

        self.doc_freqs: Dict[str, int] = {}

        self.doc_lengths: List[int] = []

        self.avg_doc_length = 0

    def tokenize(
        self,
        text: str,
    ) -> List[str]:

        return text.lower().split()

    def fit(
        self,
        chunks: List[Dict],
    ):

        self.documents = chunks

        self.doc_tokens = []

        self.doc_freqs = {}

        self.doc_lengths = []

        for chunk in chunks:

            tokens = self.tokenize(
                chunk["text"]
            )

            self.doc_tokens.append(tokens)

            self.doc_lengths.append(
                len(tokens)
            )

            for token in set(tokens):

                self.doc_freqs[token] = (
                    self.doc_freqs.get(token, 0) + 1
                )

        if self.doc_lengths:

            self.avg_doc_length = (
                sum(self.doc_lengths)
                / len(self.doc_lengths)
            )

    def score(
        self,
        query: str,
        index: int,
    ) -> float:

        tokens = self.doc_tokens[index]

        frequencies = Counter(tokens)

        score = 0.0

        N = len(self.documents)

        for term in self.tokenize(query):

            if term not in frequencies:
                continue

            df = self.doc_freqs.get(term, 1)

            idf = log(
                (N - df + 0.5)
                / (df + 0.5)
                + 1
            )

            tf = frequencies[term]

            numerator = tf * (
                self.k1 + 1
            )

            denominator = (
                tf
                + self.k1
                * (
                    1
                    - self.b
                    + self.b
                    * self.doc_lengths[index]
                    / self.avg_doc_length
                )
            )

            score += idf * (
                numerator / denominator
            )

        return score

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> List[Dict]:

        if not self.documents:

            return []

        scores = []

        for index in range(
            len(self.documents)
        ):

            scores.append(
                (
                    self.score(
                        query,
                        index,
                    ),
                    index,
                )
            )

        scores.sort(
            reverse=True,
            key=lambda x: x[0],
        )

        results = []

        for score, index in scores[:top_k]:

            document = dict(
                self.documents[index]
            )

            document["bm25_score"] = round(
                score,
                4,
            )

            results.append(document)

        return results