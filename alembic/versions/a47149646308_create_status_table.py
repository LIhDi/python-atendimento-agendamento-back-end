"""create status table

Revision ID: a47149646308
Revises: 45e479e5bedf
Create Date: 2021-02-28 13:25:27.567958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a47149646308'
down_revision = '45e479e5bedf'
branch_labels = None
depends_on = None


def upgrade():
    status = op.create_table(
            'status',
            sa.Column('id_int', sa.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True),
            sa.Column('name', sa.String(length=128)),
            sa.Column('code', sa.String(length=128)),
            sa.Column('description', sa.String(length=256)),
            sa.Column('dflag', sa.Boolean(), nullable=False, default=False),
            sa.Column('updated_at', sa.DateTime()),
            sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'))
            )
    op.bulk_insert(status,
                   [
                     {'name': 'HORÁRIO DISPONIVEL', 'code': 'horario_disponivel',
                      'description': 'Horário que ainda não foi agendado'},
                     {'name': 'HORÁRIO AGENDADO', 'code': 'horario_agendado',
                      'description': 'Horário que foi agendado'},
                     {'name': 'FINALIZADO COM SUCESSO', 'code': 'finalizado_com_sucesso',
                      'description': 'Atendimento finalizado com sucesso'},
                     {'name': 'NÃO COMPARECIMENTO', 'code': 'nao_comparecimento',
                      'description': 'Pessoa não compareceu'},
                     {'name': 'HORÁRIO AGENDADO', 'code': 'horario_agendado',
                      'description': 'Pessoa agendou um horário'}
                     ]
                   )


def downgrade():
    op.drop_table("status")
