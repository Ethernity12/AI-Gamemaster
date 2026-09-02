from uuid import UUID
from app.database.models.sessions import Session
from app.database.repositories.session_repository import SessionRepository


class SessionService:
    def __init__(self, repository: SessionRepository):
        self._repository = repository
        
    async def create_session(self, title: str, setting: str | None) -> Session:
        created_session = await self._repository.create(title=title, setting=setting)
        return created_session

    async def get_session(self, session_id: UUID) -> Session | None:
        return await self._repository.get(session_id)
    
    async def update_session(self, session_id: UUID, **values) -> Session | None:
        session = await self._repository.get(session_id)
        if session is None:
            return None

        upd_values = {k: v for k, v in values.items() if v is not None}
        
        updated_session = await self._repository.update(session_id, **upd_values)
        return updated_session
    
    async def delete_session(self, session_id: UUID) -> None:
        await self._repository.delete(session_id)