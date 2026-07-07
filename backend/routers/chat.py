from fastapi import APIRouter

from services.rag_pipeline import RAGPipeline

router = APIRouter()

pipeline = RAGPipeline()


@router.post("/")
def ask(
    request: dict,
):

    question = request.get(
        "question",
        "",
    )

    top_k = request.get(
        "top_k",
        5,
    )

    return pipeline.ask(
        question,
        top_k,
    )