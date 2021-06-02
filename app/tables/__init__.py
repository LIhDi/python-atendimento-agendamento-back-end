import sqlalchemy

metadata = sqlalchemy.MetaData()

appointment_status = sqlalchemy.Table(
    "appointment_status",
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

schedule_status = sqlalchemy.Table(
    "schedule_status",
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

attendance_status = sqlalchemy.Table(
    "attendance_status",
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

units = sqlalchemy.Table(
    "units",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=128)),
    sqlalchemy.Column("code", sqlalchemy.String(length=128)),
    sqlalchemy.Column("email", sqlalchemy.String(length=128)),
    sqlalchemy.Column("phone", sqlalchemy.String(length=128)),
    sqlalchemy.Column("description", sqlalchemy.String(length=256)),
    sqlalchemy.Column("attendants_number", sqlalchemy.Integer()),
    sqlalchemy.Column("active", sqlalchemy.Boolean()),
    sqlalchemy.Column("dflag", sqlalchemy.Boolean()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime())
)

appointments = sqlalchemy.Table(
    "appointments",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(sqlalchemy.ForeignKey("subjects.id_int"), type_=sqlalchemy.Integer, name="id_subject"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("schedules.id_int"), type_=sqlalchemy.Integer, name="id_schedule"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("attendances.id_int"), type_=sqlalchemy.Integer, name="id_attendance"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("appointment_status.id_int"), type_=sqlalchemy.Integer, name="id_appointment_status"),
    sqlalchemy.Column("name", sqlalchemy.String(length=128)),
    sqlalchemy.Column("email", sqlalchemy.String(length=128)),
    sqlalchemy.Column("national_registration", sqlalchemy.String(length=32)),
    sqlalchemy.Column("arrived_at", sqlalchemy.DateTime()),
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

schedules = sqlalchemy.Table(
    "schedules",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(sqlalchemy.ForeignKey("units.id_int"), type_=sqlalchemy.Integer, name="id_unit"),
    sqlalchemy.Column(sqlalchemy.ForeignKey("schedule_status.id_int"), type_=sqlalchemy.Integer, name="id_schedule_status"),
    sqlalchemy.Column("id_employee", sqlalchemy.String(length=128)),
    sqlalchemy.Column("schedule_date", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),

)

attendances = sqlalchemy.Table(
    "attendances",
    metadata,
    sqlalchemy.Column("id_int", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(sqlalchemy.ForeignKey("attendance_status.id_int"), type_=sqlalchemy.Integer, name="id_attendance_status"),
    sqlalchemy.Column("id_employee", sqlalchemy.String(length=128)),
    sqlalchemy.Column("rating", sqlalchemy.Integer()),
    sqlalchemy.Column("start_time", sqlalchemy.DateTime()),
    sqlalchemy.Column("end_time", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime()),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime()),

)






