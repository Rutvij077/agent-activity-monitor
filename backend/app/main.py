
from fastapi import FastAPI
from backend.app.config import settings
from backend.app.schemas.health import HealthResponse

app = FastAPI(
    title=settings.APP_NAME,
    description="Monitor AI agent executions, token usage, costs and performance.",
    version="1.0.0"
)


@app.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "healthy",
        "message": "AI Agent Monitor API is running"
    }
