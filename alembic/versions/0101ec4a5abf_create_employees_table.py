"""create employees table

Revision ID: 0101ec4a5abf
Revises: 
Create Date: 2021-02-28 13:22:59.045261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0101ec4a5abf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'employees',
            sa.Column('id_int', sa.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
            )


def downgrade():
    op.drop_table("employees")
