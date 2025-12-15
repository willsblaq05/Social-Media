"""add content column to post table

Revision ID: 1d8aed376773
Revises: fb6f4fcf2756
Create Date: 2025-12-05 07:53:06.549119

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d8aed376773'
down_revision: Union[str, Sequence[str], None] = 'fb6f4fcf2756'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False ))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
