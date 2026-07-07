from __future__ import annotations

import google.generativeai as genai

from config.settings import (
    GOOGLE_API_KEY,
    GEMINI_MODEL,
)
from utils.logger import log


class GeminiLLM:
    """
    Enterprise Gemini LLM

    Features
    --------
    ✓ Context-aware responses
    ✓ Production prompt
    ✓ Temperature control
    ✓ Error handling
    """

    def __init__(self):

        if not GOOGLE_API_KEY:
            raise ValueError(
                "GOOGLE_API_KEY not found."
            )

        genai.configure(
            api_key=GOOGLE_API_KEY
        )

        self.model = genai.GenerativeModel(
            GEMINI_MODEL
        )

        log.info(
            "Gemini LLM initialized."
        )

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:

        prompt = f"""
You are an Enterprise AI Assistant.

Use ONLY the information provided in the context below.

Rules:
- Do not hallucinate.
- If the answer is not present in the context, reply:
  "I couldn't find that information in the uploaded documents."
- Answer clearly using bullet points whenever appropriate.
- Keep answers professional and concise.

======================
CONTEXT
======================

{context}

======================
QUESTION
======================

{question}

======================
ANSWER
======================
"""

        try:

            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.2,
                    "top_p": 0.9,
                    "max_output_tokens": 1024,
                },
            )

            answer = (
                response.text.strip()
                if hasattr(response, "text")
                else "No response generated."
            )

            log.info(
                "Gemini response generated."
            )

            return answer

        except Exception as exc:

            log.exception(exc)

            return (
                "An error occurred while generating the answer."
            )