"""Renaming students to scholars

Revision ID: 39f482773b26
Revises: c0f612638bf7
Create Date: 2025-05-28 08:30:53.664348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39f482773b26'
down_revision = 'c0f612638bf7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
