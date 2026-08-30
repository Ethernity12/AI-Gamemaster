from fastapi import APIRouter, Request
from app.api.schemas.chat import ChatRequest, ChatResponse
from app.llm.data_models import GenerationConfig, Message


router = APIRouter()


@router.post("", response_model=ChatResponse)
async def chat_endpoint(request: Request, payload: ChatRequest) -> ChatResponse:
    llm = request.app.state.llm
    
    response = await llm.generate(
        [Message(role='user', content=payload.prompt)], GenerationConfig(max_tokens=2048)
    )

    return ChatResponse(response=response)