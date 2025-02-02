"""Create phone number for user column

Revision ID: 22cca44dd0e3
Revises: 
Create Date: 2025-01-08 19:09:50.000933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22cca44dd0e3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
   op.drop_column('users', 'phone_number')
