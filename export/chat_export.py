from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List

from config.settings import DATA_FOLDER


class ChatExporter:
    """
    Enterprise Chat Export

    Export conversation to Markdown.

    Future

    • PDF
    • DOCX
    • HTML
    """

    EXPORT_FOLDER = DATA_FOLDER / "exports"

    @classmethod
    def export(
        cls,
        history: List[dict],
    ) -> Path:

        cls.EXPORT_FOLDER.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = (
            datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
            + ".md"
        )

        output = cls.EXPORT_FOLDER / filename

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                "# Enterprise AI Chat Export\n\n"
            )

            for message in history:

                role = message["role"].upper()

                content = message["content"]

                file.write(
                    f"## {role}\n\n"
                )

                file.write(content)

                file.write("\n\n")

        return output