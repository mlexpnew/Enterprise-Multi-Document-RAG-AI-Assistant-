from pathlib import Path

from pypdf import PdfReader


class PDFLoader:

    @staticmethod
    def load(file_path):

        reader = PdfReader(file_path)

        pages = []

        for page_number, page in enumerate(reader.pages, start=1):

            text = page.extract_text()

            if text:

                pages.append(
                    {
                        "page": page_number,
                        "text": text,
                    }
                )

        return pages