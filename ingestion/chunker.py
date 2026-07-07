from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class ChunkService:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
        )

    def split(self, pages):

        chunks = []

        for page in pages:

            texts = self.splitter.split_text(page["text"])

            for chunk in texts:

                chunks.append(
                    {
                        "text": chunk,
                        "page": page["page"],
                    }
                )

        return chunks