from uuid import UUID
from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: UUID
    prompt: str


class ChatResponse(BaseModel):
    response: str
    
class ChatHistoryRequest(BaseModel):
    session_id: UUID
    
class ChatHistoryResponse(BaseModel):
    history: list[dict]