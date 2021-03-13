"""create appointments table

Revision ID: 28f769ec8fec
Revises: 4b49a691162d
Create Date: 2021-02-28 13:28:38.266807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f769ec8fec'
down_revision = '4b49a691162d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            "appointments",
            sa.Column("id_int", sa.Integer, primary_key=True),
            sa.Column(sa.ForeignKey("units.id_int"), type_=sa.Integer, name="id_unit", nullable=False),
            sa.Column(sa.ForeignKey("persons.id_int"), type_=sa.Integer, name="id_person", nullable=False),
            sa.Column(sa.ForeignKey("subjects.id_int"), type_=sa.Integer, name="id_subject", nullable=False),
            sa.Column(sa.ForeignKey("employees.id_int"), type_=sa.Integer, name="id_employee", nullable=True),
            sa.Column(sa.ForeignKey("status.id_int"), type_=sa.Integer, name="id_status", nullable=False),
            sa.Column("name", sa.String(length=128)),
            sa.Column("attendance_number", sa.String(length=32)),
            sa.Column("national_registration", sa.String(length=32)),
            sa.Column("unit", sa.String(length=128)),
            sa.Column("shift", sa.String(length=8)),
            sa.Column("appointment_date", sa.DateTime()),
            sa.Column("formatted_date", sa.String(length=32)),
            sa.Column("formatted_time", sa.String(length=32)),
            sa.Column("formatted_day", sa.String(length=32)),
            sa.Column("arrival_time", sa.DateTime()),
            sa.Column("start_time", sa.DateTime()),
            sa.Column("end_time", sa.DateTime()),
            sa.Column("updated_at", sa.DateTime()),
            sa.Column("created_at", sa.DateTime(), server_default=sa.text('now()')),
            )


def downgrade():
  op.drop_table("appointments")
