"""create subjects table

Revision ID: 470b8aebe2fd
Revises: a47149646308
Create Date: 2021-02-28 13:26:36.557573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '470b8aebe2fd'
down_revision = 'a47149646308'
branch_labels = None
depends_on = None


def upgrade():
    subjects = op.create_table(
            'subjects',
            sa.Column('id_int', sa.Integer, primary_key=True, nullable=False, unique=True, autoincrement=True),
            sa.Column('name', sa.String(length=128)),
            sa.Column('code', sa.String(length=128)),
            sa.Column('description', sa.String(length=256)),
            sa.Column('active', sa.Boolean(), nullable=False, default=True),
            sa.Column('dflag', sa.Boolean(), nullable=False, default=False),
            sa.Column('updated_at', sa.DateTime()),
            sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'))
            )
    op.bulk_insert(subjects,
                   [
                     {'name': 'REGISTRO DE PROFISSIONAL', 'code': 'code_1', 'description': 'Registro de Profissional'},
                     {'name': 'AUTENTIFICÃO DE DOCUMENTOS', 'code': 'code_2',
                      'description': 'Autenticação de Documentos'},
                     {'name': 'VALIDAÇÃO DE DIPLOMAS', 'code': 'code_3', 'description': 'Validação de Diplomas'},
                     {'name': 'NOVO REGISTRO', 'code': 'code_4', 'description': 'Novo Registro'},
                     ]
                   )


def downgrade():
  op.drop_table("subjects")
