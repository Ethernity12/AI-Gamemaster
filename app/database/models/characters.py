from uuid import uuid4, UUID
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class Character(Base):
    __tablename__ = "characters"
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = String(255)
    appearance: Mapped[str | None] = mapped_column(Text, nullable=True)
    personality: Mapped [str | None] = mapped_column(Text, nullable=True)
    background: Mapped [str | None] = mapped_column(Text, nullable=True)
    