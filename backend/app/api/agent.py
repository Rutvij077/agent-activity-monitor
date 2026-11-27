
from fastapi import APIRouter
from uuid import uuid4

from backend.app.schemas.agent import (
    AgentRunRequest,
    AgentRunResponse
)

router = APIRouter()


@router.post("/agent/run", response_model=AgentRunResponse)
def run_agent(request: AgentRunRequest):

    execution_id = str(uuid4())

    return AgentRunResponse(
        execution_id=execution_id,
        status="completed",
        message="Agent execution completed"
    )

