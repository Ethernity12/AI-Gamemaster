from uuid import UUID
from fastapi import APIRouter, HTTPException, Request
from app.api.schemas.session import SessionRequest, SessionResponse, SessionUpdateRequest
from app.database.models.sessions import Session
from app.services.session_service import SessionService


router = APIRouter()

@router.post("", response_model=SessionResponse)
async def session_create(request: Request, payload: SessionRequest) -> SessionResponse:
    session_service: SessionService = request.app.state.session_service
    return await session_service.create(title=payload.title, setting=payload.setting)

@router.delete("/{session_id}")
async def session_delete(request: Request, session_id: UUID) -> None:
    pass

@router.patch("/{session_id}", response_model=SessionResponse)
async def session_update(request: Request, session_id: UUID, payload: SessionUpdateRequest) -> SessionResponse:
    pass

@router.get("/{session_id}", response_model=SessionResponse)
async def session_get(request: Request, session_id: UUID) -> SessionResponse:
    session: Session | None = await request.app.state.session_service.get(session_id)

    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return session