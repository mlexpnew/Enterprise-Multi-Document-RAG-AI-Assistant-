from pathlib import Path

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from config.settings import DATA_FOLDER
from ingestion.ingest import DocumentIngestion

router = APIRouter()

pipeline = DocumentIngestion()


@router.post("/")
async def upload(
    file: UploadFile = File(...),
):

    DATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True,
    )

    path = DATA_FOLDER / file.filename

    with open(path, "wb") as f:

        f.write(
            await file.read()
        )

    chunks = pipeline.ingest(
        str(path)
    )

    return {
        "filename": file.filename,
        "chunks": chunks,
    }