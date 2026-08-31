from uuid import UUID
from app.database.connector import DatabaseConnector
from app.database.models.sessions import Session
from sqlalchemy import select, update


class SessionRepository:
    def __init__(self, db_connector: DatabaseConnector):
        self._db_connector = db_connector
        
    async def get(self, session_id: UUID) -> Session | None:
        async with self._db_connector.session() as session:
            result = await session.execute(
                select(Session).where(Session.id == session_id)
            )
            
        return result.scalar_one_or_none()
    
    async def create(self) -> Session:
        async with self._db_connector.session() as session:
            db_session = Session()

            session.add(db_session)

            await session.commit()
            await session.refresh(db_session)
            
            return db_session
        
    async def update(self, session_id: UUID, **values) -> Session:
        async with self._db_connector.session() as session:
            stmt = (
                update(Session)
                .where(Session.id == session_id)
                .values(**values)
                .returning(Session)
            )

            result = await session.execute(stmt)

            await session.commit()

            return result.scalar_one_or_none()
        
    async def delete(self, session_id: UUID) -> None:
        async with self._db_connector.session() as session:
            db_session = await session.get(Session, session_id)

            if db_session is None:
                return

            await session.delete(db_session)
            await session.commit()
        
    