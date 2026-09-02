from uuid import UUID
from fastapi import APIRouter, HTTPException, Request, status
from app.api.schemas.session import SessionRequest, SessionResponse, SessionUpdateRequest
from app.database.models.sessions import Session
from app.services.session_service import SessionService


router = APIRouter()

@router.post("", response_model=SessionResponse)
async def create_session(request: Request, payload: SessionRequest) -> SessionResponse:
    session_service: SessionService = request.app.state.session_service
    return await session_service.create_session(title=payload.title, setting=payload.setting)

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_session(request: Request, session_id: UUID) -> None:
    session_service: SessionService = request.app.state.session_service
    await session_service.delete_session(session_id)

@router.patch("/{session_id}", response_model=SessionResponse)
async def update_session(request: Request, session_id: UUID, payload: SessionUpdateRequest) -> SessionResponse:
    session_service: SessionService = request.app.state.session_service
    session: Session | None = await session_service.update_session(session_id, title=payload.title, setting=payload.setting)

    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return session

@router.get("/{session_id}", response_model=SessionResponse)
async def get_session(request: Request, session_id: UUID) -> SessionResponse:
    session_service: SessionService = request.app.state.session_service
    session: Session | None = await session_service.get_session(session_id)

    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    return session