from __future__ import annotations

from typing import Dict

import pandas as pd

from analytics.document_stats import DocumentStatistics
from analytics.query_logger import QueryLogger
from feedback.feedback_storage import FeedbackStorage


class AnalyticsDashboard:
    """
    Enterprise Analytics Dashboard

    Features
    --------
    ✓ Total Documents
    ✓ Indexed Chunks
    ✓ Total Queries
    ✓ Average Confidence
    ✓ Average Response Time
    ✓ Positive Feedback
    ✓ Negative Feedback
    ✓ Success Rate
    ✓ Storage Usage
    """

    def __init__(self):

        self.document_stats = DocumentStatistics()

    def feedback_summary(self) -> Dict:

        try:

            df = FeedbackStorage.load()

        except Exception:

            return {
                "Positive Feedback": 0,
                "Negative Feedback": 0,
                "Feedback Received": 0,
            }

        positive = len(
            df[df["rating"] == "Positive"]
        )

        negative = len(
            df[df["rating"] == "Negative"]
        )

        return {

            "Positive Feedback": positive,

            "Negative Feedback": negative,

            "Feedback Received": len(df),
        }

    def query_summary(self) -> Dict:

        try:

            total_queries = QueryLogger.total_queries()

            avg_confidence = (
                QueryLogger.average_confidence()
            )

            avg_latency = (
                QueryLogger.average_latency()
            )

        except Exception:

            total_queries = 0

            avg_confidence = 0

            avg_latency = 0

        return {

            "Total Queries": total_queries,

            "Average Confidence": avg_confidence,

            "Average Latency (s)": avg_latency,
        }

    def success_rate(self) -> float:

        try:

            queries = QueryLogger.total_queries()

            feedback = self.feedback_summary()

            positive = feedback[
                "Positive Feedback"
            ]

            if queries == 0:

                return 0

            return round(
                positive / queries * 100,
                2,
            )

        except Exception:

            return 0

    def summary(self) -> Dict:

        summary = {}

        summary.update(
            self.document_stats.summary()
        )

        summary.update(
            self.query_summary()
        )

        summary.update(
            self.feedback_summary()
        )

        summary["Success Rate (%)"] = (
            self.success_rate()
        )

        return summary

    def dataframe(self) -> pd.DataFrame:

        summary = self.summary()

        return pd.DataFrame(
            {
                "Metric": summary.keys(),
                "Value": summary.values(),
            }
        )

    def print_summary(self):

        print("\n")

        print("=" * 60)

        print("Enterprise Analytics Dashboard")

        print("=" * 60)

        for key, value in self.summary().items():

            print(f"{key:<30} : {value}")

        print("=" * 60)