from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

GENERATION_MODEL = os.getenv(
    "GENERATION_MODEL",
    "gemini-2.5-flash"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "gemini-embedding-001"
)

DATA_FOLDER = BASE_DIR / os.getenv(
    "DATA_FOLDER",
    "data"
)

CHROMA_DB = BASE_DIR / os.getenv(
    "CHROMA_DB",
    "chroma_db"
)

LOG_FOLDER = BASE_DIR / os.getenv(
    "LOG_FOLDER",
    "logs"
)

TOP_K = int(os.getenv("TOP_K", 5))

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1200))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 200))

SUPPORTED_FILES = [
    ".pdf",
    ".txt",
    ".md"
]

APP_TITLE = "Enterprise RAG AI Assistant"

PAGE_ICON = "🤖"

PAGE_LAYOUT = "wide"

for folder in [
    DATA_FOLDER,
    CHROMA_DB,
    LOG_FOLDER,
]:
    folder.mkdir(exist_ok=True)