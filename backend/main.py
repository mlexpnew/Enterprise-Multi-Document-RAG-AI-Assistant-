from fastapi import FastAPI

from backend.routers.chat import router as chat_router
from backend.routers.upload import router as upload_router
from backend.routers.documents import router as document_router
from backend.routers.health import router as health_router

app = FastAPI(
    title="Enterprise Multi-Document RAG AI Assistant",
    version="1.0.0",
    description="Production Ready Enterprise RAG Backend",
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"],
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"],
)

app.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"],
)


@app.get("/")
def root():

    return {
        "application": "Enterprise Multi-Document RAG AI Assistant",
        "version": "1.0.0",
        "status": "running",
    }