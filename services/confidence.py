from __future__ import annotations

from typing import Dict, List

from utils.logger import log


class ConfidenceScore:
    """
    Enterprise Confidence Scoring

    Calculates confidence using the
    similarity scores returned by
    the Hybrid Retriever.

    Score Range
    -----------
    0 - 100%
    """

    MIN_CONFIDENCE = 0.0
    MAX_CONFIDENCE = 100.0

    @classmethod
    def calculate(
        cls,
        retrieved_chunks: List[Dict],
    ) -> float:

        if not retrieved_chunks:
            return 0.0

        scores = [
            chunk.get("score", 0)
            for chunk in retrieved_chunks
        ]

        if not scores:
            return 0.0

        average_score = sum(scores) / len(scores)

        confidence = average_score * 100

        confidence = max(
            cls.MIN_CONFIDENCE,
            min(cls.MAX_CONFIDENCE, confidence),
        )

        confidence = round(confidence, 2)

        log.info(
            "Confidence Score: {}%",
            confidence,
        )

        return confidence

    @classmethod
    def level(
        cls,
        confidence: float,
    ) -> str:

        if confidence >= 90:
            return "Excellent"

        if confidence >= 75:
            return "High"

        if confidence >= 60:
            return "Medium"

        if confidence >= 40:
            return "Low"

        return "Very Low"

    @classmethod
    def summary(
        cls,
        retrieved_chunks: List[Dict],
    ) -> Dict:

        score = cls.calculate(
            retrieved_chunks
        )

        return {
            "score": score,
            "level": cls.level(score),
        }