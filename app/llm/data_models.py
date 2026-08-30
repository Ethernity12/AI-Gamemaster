from typing import Any, Literal
from pydantic import BaseModel, Field


class GenerationConfig(BaseModel):
    max_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.9
    
    extra_body: dict[str, Any] = Field(default_factory=dict)
    
class Message:
    role: Literal["system", "user", "assistant", "tool"]
    content: str