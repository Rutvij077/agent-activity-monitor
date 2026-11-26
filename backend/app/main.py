
from fastapi import FastAPI
from backend.app.config import settings
from backend.app.api.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Monitor AI agent executions, token usage, costs and performance.",
    version="1.0.0"
)

app.include_router(health_router)
