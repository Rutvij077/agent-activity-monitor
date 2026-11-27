
from pydantic import BaseModel


class AgentRunRequest(BaseModel):
    input_text: str


class AgentRunResponse(BaseModel):
    execution_id: str
    status: str
    message: str
