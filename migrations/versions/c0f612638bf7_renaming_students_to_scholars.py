"""Renaming students to scholars

Revision ID: c0f612638bf7
Revises: bd25a1fb36e0
Create Date: 2025-05-28 08:29:36.167434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0f612638bf7'
down_revision = 'bd25a1fb36e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
