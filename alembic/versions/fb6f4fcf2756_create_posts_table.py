"""create posts table

Revision ID: fb6f4fcf2756
Revises: 
Create Date: 2025-12-05 07:34:40.067860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb6f4fcf2756'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,primary_key=True),
                     sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
