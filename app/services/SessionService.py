from uuid import UUID
from app.database.models.sessions import Session
from app.database.repositories.session_repository import SessionRepository


class SessionService:
    def __init__(self, repository: SessionRepository):
        self._repository = repository
        
    async def create(self) -> Session:
        return await self._repository.create()

    async def get(self, session_id: UUID) -> Session | None:
        return await self._repository.get(session_id)