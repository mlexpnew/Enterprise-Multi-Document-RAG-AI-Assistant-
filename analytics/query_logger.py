from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd

from config.settings import DATA_FOLDER


class QueryLogger:
    """
    Enterprise Query Logger

    Logs every user query and response.

    Future
    -------
    • Analytics Dashboard
    • User Behaviour
    • Most Asked Questions
    """

    LOG_FILE = DATA_FOLDER / "query_logs.csv"

    @classmethod
    def initialize(cls):

        if not cls.LOG_FILE.exists():

            df = pd.DataFrame(
                columns=[
                    "timestamp",
                    "question",
                    "response_length",
                    "confidence",
                    "latency",
                ]
            )

            df.to_csv(
                cls.LOG_FILE,
                index=False,
            )

    @classmethod
    def log(
        cls,
        question: str,
        answer: str,
        confidence: float,
        latency: float,
    ):

        cls.initialize()

        row = pd.DataFrame(
            [
                {
                    "timestamp": datetime.now(),
                    "question": question,
                    "response_length": len(answer),
                    "confidence": confidence,
                    "latency": latency,
                }
            ]
        )

        row.to_csv(
            cls.LOG_FILE,
            mode="a",
            header=False,
            index=False,
        )

    @classmethod
    def history(cls) -> pd.DataFrame:

        cls.initialize()

        return pd.read_csv(cls.LOG_FILE)

    @classmethod
    def total_queries(cls) -> int:

        return len(cls.history())

    @classmethod
    def average_confidence(cls) -> float:

        df = cls.history()

        if df.empty:
            return 0

        return round(
            df["confidence"].mean(),
            2,
        )

    @classmethod
    def average_latency(cls) -> float:

        df = cls.history()

        if df.empty:
            return 0

        return round(
            df["latency"].mean(),
            2,
        )