"""add course level

Revision ID: 0002
Revises: 0001
Create Date: 2026-11-06 13:36:36.291107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0002'
down_revision: Union[str, Sequence[str], None] = '0001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Step 1: add column as nullable first (table already has rows)
    op.add_column('courses', sa.Column('level', sa.Text(), nullable=True))
    # Step 2: fill existing rows — elective courses get 'beginner', others 'intermediate'
    op.execute(
        "UPDATE courses SET level = CASE WHEN is_elective THEN 'beginner' "
        "ELSE 'intermediate' END"
    )
    # Step 3: now forbid NULL
    op.alter_column('courses', 'level', nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('courses', 'level')
