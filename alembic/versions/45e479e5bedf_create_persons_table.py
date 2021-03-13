"""create persons table

Revision ID: 45e479e5bedf
Revises: 0101ec4a5abf
Create Date: 2021-02-28 13:23:33.273171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e479e5bedf'
down_revision = '0101ec4a5abf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'persons',
        sa.Column('id_int', sa.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True),
        sa.Column('national_registration', sa.String(length=32), nullable=False, unique=True),
        sa.Column('email', sa.String(length=128))
        )


def downgrade():
  op.drop_table("persons")