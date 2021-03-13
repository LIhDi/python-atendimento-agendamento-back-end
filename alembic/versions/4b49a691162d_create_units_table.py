"""create units table

Revision ID: 4b49a691162d
Revises: 470b8aebe2fd
Create Date: 2021-02-28 13:27:27.003460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b49a691162d'
down_revision = '470b8aebe2fd'
branch_labels = None
depends_on = None


def upgrade():
  units = op.create_table(
          'units',
          sa.Column('id_int', sa.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True),
          sa.Column('name', sa.String(length=128)),
          sa.Column('code', sa.String(length=128)),
          sa.Column('email', sa.String(length=128)),
          sa.Column('phone', sa.String(length=128)),
          sa.Column('description', sa.String(length=256)),
          sa.Column('active', sa.Boolean(), nullable=False, default=True),
          sa.Column('dflag', sa.Boolean(), nullable=False, default=False),
          sa.Column('updated_at', sa.DateTime()),
          sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'))
          )
  op.bulk_insert(units,
                 [
                   {'name': 'ANGRA DOS REIS', 'code': 'angra_dos_reis',
                    'description': 'Unidade Central de Angra dos Reis',
                    'email': 'unidade_angra@gmail.com', 'phone': '21 3097-3453'},
                   {'name': 'RIO DE JANEIRO', 'code': 'rio_de_janeiro',
                    'description': 'Unidade Central do Rio de Janeiro',
                    'email': 'unidade_rio@gmail.com', 'phone': '21 3097-0000'},
                   ]
                 )


def downgrade():
  op.drop_table("units")
