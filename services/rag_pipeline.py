from __future__ import annotations

from retriever.hybrid_search import HybridRetriever
from services.confidence import ConfidenceScore
from services.context_builder import ContextBuilder
from llm.gemini import GeminiLLM
from utils.logger import log


class RAGPipeline:
    """
    Enterprise Multi-Document RAG Pipeline

    Flow
    ----
    User Question
        ↓
    Hybrid Retriever
        ↓
    Context Builder
        ↓
    Gemini LLM
        ↓
    Confidence Score
        ↓
    Final Response
    """

    def __init__(self):

        self.retriever = HybridRetriever()

        self.context_builder = ContextBuilder()

        self.llm = GeminiLLM()

        self.confidence = ConfidenceScore()

    def ask(
        self,
        question: str,
        top_k: int = 5,
    ):

        log.info(
            "Question received: {}",
            question,
        )

        retrieved_chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k,
        )

        if not retrieved_chunks:

            return {
                "answer": (
                    "I couldn't find any relevant information "
                    "in the uploaded documents."
                ),
                "citations": [],
                "confidence": 0,
            }

        context, citations = self.context_builder.build(
            retrieved_chunks
        )

        answer = self.llm.generate(
            question=question,
            context=context,
        )

        confidence = self.confidence.calculate(
            retrieved_chunks
        )

        log.info(
            "Answer generated successfully."
        )

        return {
            "answer": answer,
            "citations": citations,
            "confidence": confidence,
        }