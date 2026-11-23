
from fastapi import FastAPI

app = FastAPI(
    title="AI Agent Execution Monitor",
    description="Monitor AI agent executions, token usage, costs and performance.",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "AI Agent Monitor API is running"
    }
