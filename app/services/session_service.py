from uuid import UUID
from app.database.models.sessions import Session
from app.database.repositories.session_repository import SessionRepository


class SessionService:
    def __init__(self, repository: SessionRepository):
        self._repository = repository
        
    async def create(self, title: str, setting: str | None) -> Session:
        created_session = await self._repository.create(title=title, setting=setting)
        return created_session

    async def get(self, session_id: UUID) -> Session | None:
        return await self._repository.get(session_id)