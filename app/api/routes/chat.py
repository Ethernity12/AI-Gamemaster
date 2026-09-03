from fastapi import APIRouter, Request
from app.api.schemas.chat import ChatHistoryRequest, ChatHistoryResponse, ChatRequest, ChatResponse
from app.llm.data_models import GenerationConfig, Message
from app.services.chat_service import ChatService


router = APIRouter()


@router.post("", response_model=ChatResponse)
async def generate(request: Request, payload: ChatRequest) -> ChatResponse:
    chat_service: ChatService = request.app.state.chat_service
    chat_service.create_user_message(payload.session_id, payload.prompt)
    response = chat_service.generate_response(payload.session_id, payload.prompt)
    return ChatResponse(response=response)

@router.get("", response_model=ChatHistoryResponse)
async def chat_history(request: Request, payload: ChatHistoryRequest) -> ChatHistoryResponse:
    chat_service: ChatService = request.app.state.chat_service
    messages = chat_service.get_history(payload.session_id)
    return ChatHistoryResponse(messages=messages)