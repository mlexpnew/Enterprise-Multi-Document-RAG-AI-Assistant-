from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class EvaluationResult:
    relevance: float
    completeness: float
    confidence: float
    overall: float


class RAGEvaluator:
    """
    Enterprise RAG Evaluation

    Evaluates answer quality based on
    retrieval confidence and answer length.

    Future:
    --------
    • RAGAS
    • DeepEval
    • LLM-as-a-Judge
    """

    @staticmethod
    def evaluate(
        answer: str,
        retrieved_chunks: List[Dict],
    ) -> EvaluationResult:

        if not answer.strip():

            return EvaluationResult(
                relevance=0,
                completeness=0,
                confidence=0,
                overall=0,
            )

        scores = [
            chunk.get("score", 0)
            for chunk in retrieved_chunks
        ]

        confidence = (
            sum(scores) / len(scores)
            if scores
            else 0
        )

        length_score = min(
            len(answer) / 400,
            1,
        )

        relevance = confidence

        completeness = length_score

        overall = (
            relevance * 0.5
            + completeness * 0.5
        )

        return EvaluationResult(
            relevance=round(
                relevance * 100,
                2,
            ),
            completeness=round(
                completeness * 100,
                2,
            ),
            confidence=round(
                confidence * 100,
                2,
            ),
            overall=round(
                overall * 100,
                2,
            ),
        )

    @staticmethod
    def as_dict(
        result: EvaluationResult,
    ) -> Dict:

        return {
            "Relevance": result.relevance,
            "Completeness": result.completeness,
            "Confidence": result.confidence,
            "Overall Score": result.overall,
        }