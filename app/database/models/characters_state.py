from uuid import UUID, uuid4
from sqlalchemy import ForeignKey, Nullable, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class CharacterState(Base):
    __tablename__ = "character_states"
    
    __table_args__ = (
        UniqueConstraint(
            "session_id",
            "character_id",
            name="uq_character_state_session_character"
        ),
    )
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    session_id: Mapped[UUID] = mapped_column(ForeignKey("sessions.id"), nullable=False)
    character_id: Mapped[UUID] = mapped_column(ForeignKey("characters.id"), nullable=False)
    state: Mapped[dict] = mapped_column(JSONB, default=dict, nullable=False)