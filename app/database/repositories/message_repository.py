import select
from uuid import UUID
from app.database.connector import DatabaseConnector
from app.database.models.messages import Message


class MessageRepository:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector = db_connector

    async def get(self, session_id: UUID, limit: int) -> list[Message]:
        async with self.db_connector.session() as session:
            result = await session.execute(
                select(Message).where(Message.session_id == session_id).limit(limit)
            )
            
            return result.scalars().all()
        
    async def create(self, message: Message) -> Message:
        async with self.db_connector.session() as session:
            session.add(message)
            await session.commit()
            await session.refresh(message)
            return message