from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health():

    return {
        "status": "healthy"
    }


@router.get("/ready")
def ready():

    return {
        "ready": True
    }