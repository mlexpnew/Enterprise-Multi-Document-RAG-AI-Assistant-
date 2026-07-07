from fastapi import APIRouter

from document.document_manager import DocumentManager

router = APIRouter()

manager = DocumentManager()


@router.get("/")
def documents():

    return manager.summary()


@router.get("/stats")
def stats():

    return manager.collection_summary()