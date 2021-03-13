import sqlalchemy

metadata = sqlalchemy.MetaData()

status = sqlalchemy.Table(
    "status",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=128)),
    sqlalchemy.Column("code", sqlalchemy.String(length=128)),
    sqlalchemy.Column("description", sqlalchemy.String(length=256)),
    sqlalchemy.Column("dflag", sqlalchemy.Boolean()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime())
)

units = sqlalchemy.Table(
    "units",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=128)),
    sqlalchemy.Column("code", sqlalchemy.String(length=128)),
    sqlalchemy.Column("description", sqlalchemy.String(length=256)),
    sqlalchemy.Column("email", sqlalchemy.String(length=128)),
    sqlalchemy.Column("phone", sqlalchemy.String(length=128)),
    sqlalchemy.Column("active", sqlalchemy.Boolean()),
    sqlalchemy.Column("dflag", sqlalchemy.Boolean()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime())
)

appointments = sqlalchemy.Table(
    "appointments",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(sqlalchemy.ForeignKey("persons.id_int"), type_=sqlalchemy.Integer, name="id_person"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("units.id_int"), type_=sqlalchemy.Integer, name="id_unit"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("status.id_int"), type_=sqlalchemy.Integer, name="id_status"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("employees.id_int"), type_=sqlalchemy.Integer, name="id_employee"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("subjects.id_int"), type_=sqlalchemy.Integer, name="id_subject"),
    sqlalchemy.Column("name", sqlalchemy.String(length=128)),
    sqlalchemy.Column("attendance_number", sqlalchemy.String(length=32)),
    sqlalchemy.Column("national_registration", sqlalchemy.String(length=32)),
    sqlalchemy.Column("unit", sqlalchemy.String(length=128)),
    sqlalchemy.Column("shift", sqlalchemy.String(length=8)),
    sqlalchemy.Column("formatted_date", sqlalchemy.String(length=32)),
    sqlalchemy.Column("formatted_time", sqlalchemy.String(length=32)),
    sqlalchemy.Column("formatted_day", sqlalchemy.String(length=32)),
    sqlalchemy.Column("appointment_date", sqlalchemy.DateTime()),
    sqlalchemy.Column("arrival_time", sqlalchemy.DateTime()),
    sqlalchemy.Column("start_time", sqlalchemy.DateTime()),
    sqlalchemy.Column("end_time", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),

)

subjects = sqlalchemy.Table(
    "subjects",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=128)),
    sqlalchemy.Column("code", sqlalchemy.String(length=128)),
    sqlalchemy.Column("description", sqlalchemy.String(length=256)),
    sqlalchemy.Column("active", sqlalchemy.Boolean()),
    sqlalchemy.Column("dflag", sqlalchemy.Boolean()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime())
)

persons = sqlalchemy.Table(
    "persons",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("national_registration", sqlalchemy.String(length=32)),
    sqlalchemy.Column("email", sqlalchemy.String(length=128))
)

employees = sqlalchemy.Table(
    "employees",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True)
)






