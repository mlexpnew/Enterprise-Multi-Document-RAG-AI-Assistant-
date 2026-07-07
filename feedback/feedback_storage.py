from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd

from config.settings import DATA_FOLDER


class FeedbackStorage:
    """
    Stores user feedback for generated answers.
    """

    FILE = DATA_FOLDER / "feedback.csv"

    @classmethod
    def initialize(cls):

        if cls.FILE.exists():
            return

        cls.FILE.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        pd.DataFrame(
            columns=[
                "timestamp",
                "question",
                "answer",
                "rating",
                "comment",
            ]
        ).to_csv(
            cls.FILE,
            index=False,
        )

    @classmethod
    def save(
        cls,
        question: str,
        answer: str,
        rating: str,
        comment: str = "",
    ):

        cls.initialize()

        row = pd.DataFrame(
            [
                {
                    "timestamp": datetime.now(),
                    "question": question,
                    "answer": answer,
                    "rating": rating,
                    "comment": comment,
                }
            ]
        )

        row.to_csv(
            cls.FILE,
            mode="a",
            header=False,
            index=False,
        )

    @classmethod
    def load(cls):

        cls.initialize()

        return pd.read_csv(cls.FILE)