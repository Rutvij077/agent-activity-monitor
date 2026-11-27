
from fastapi import APIRouter
from backend.app.schemas.health import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        "message": "AI Agent Monitor API is running"
    }
