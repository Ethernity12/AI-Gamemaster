from uuid import UUID
from fastapi import APIRouter, Request
from app.api.schemas.session import SessionRequest, SessionResponse, SessionUpdateRequest


router = APIRouter()

@router.post("", response_model=SessionResponse)
async def session_create(request: Request, payload: SessionRequest) -> SessionResponse:
    pass

@router.delete("/{session_id}")
async def session_delete(request: Request, session_id: UUID) -> None:
    pass

@router.patch("/{session_id}", response_model=SessionResponse)
async def session_update(request: Request, session_id: UUID, payload: SessionUpdateRequest) -> SessionResponse:
    pass

@router.get("/{session_id}", response_model=SessionResponse)
async def session_get(request: Request, session_id: UUID) -> SessionResponse:
    pass