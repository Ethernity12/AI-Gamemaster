from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class SessionRequest(BaseModel):
    title: str
    setting: str | None
    
class SessionResponse(BaseModel):
    id: UUID
    title: str
    setting: str | None
    created_at: datetime
    updated_at: datetime
    
class SessionUpdateRequest(BaseModel):
    title: str | None
    setting: str | None