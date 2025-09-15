"""add cice projects mobile-app-resumen-op

Revision ID: 5dcca8d749ad
Revises: c08e2ca6e40f
Create Date: 2025-08-20 22:09:37.213089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlmodel import SQLModel, Session


# revision identifiers, used by Alembic.
revision: str = '5dcca8d749ad'
down_revision: Union[str, Sequence[str], None] = 'c08e2ca6e40f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass
    with Session(bind=op.get_bind()) as session :
        pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
