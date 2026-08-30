"""enable pgvector

Revision ID: bb3b97256be0
Revises: 6e1141bc7a6f
Create Date: 2026-08-30 23:51:42.391239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb3b97256be0'
down_revision: Union[str, Sequence[str], None] = '6e1141bc7a6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DROP EXTENSION IF EXISTS vector")
