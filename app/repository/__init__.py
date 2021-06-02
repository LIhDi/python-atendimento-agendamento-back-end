from databases import Database
from datetime import datetime
from sqlalchemy.sql import select
from exceptions import DatabaseException
from util.loggers import logger
from tables import appointment_status, appointments, units, subjects, schedules


class AtendimentoRepository:
    def __init__(self, db):
        self.db: Database = db


class AppointmentsRepository:
    def __init__(self, db):
        self.db: Database = db

    async def find_all(self):
        logger.debug("REPOSITORY find all appointments.")
        try:
            query = select([appointments]).where(appointments.c.dflag == False)
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_by_status(self, status_code, national_registration):
        logger.debug("REPOSITORY find appointments by status.")
        try:
            join = appointments.join(appointment_status)
            query = (
                select([appointments])
                    .select_from(join)
                    .where(appointments.c.national_registration == national_registration)
                    .where(appointment_status.c.code == status_code))
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_status_by_code(self, status_code):
        logger.debug("REPOSITORY find status by code.")
        try:
            query = (
                select([appointment_status])
                .where(appointment_status.c.code == status_code)
                .where(appointment_status.c.dflag == False))
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_all_status(self):
        logger.debug("REPOSITORY find all status.")
        try:
            query = select([appointment_status]).where(appointment_status.c.dflag == False)
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def cancel(self, appointment):
        logger.debug("REPOSITORY update appointment status cancelation")
        try:
            return (
                appointments.update()
                    .values(appointment)
                    .where(appointments.c.id_int == appointment["id_int"])
            )
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")
    
    def save(self, appointment):
        return appointments.insert().values(appointment)
    
    async def find_by_id(self, appointment_id):
        logger.debug("REPOSITORY find appointments by id.")
        try:
            query = (
                select([appointments])
                .where(appointments.c.id_int == appointment_id)
                .where(appointments.c.dflag == False))
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")


class UnitsRepository:
    def __init__(self, db):
        self.db: Database = db

    async def find_all(self, active):
        logger.debug("REPOSITORY find all units.")
        try:
            query = units.select().where(units.c.dflag == False)
            query = query.where(units.c.active == active) if active != None else query
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_by_code(self, code_unit):
        logger.debug("REPOSITORY find unit by code.")
        try:
            query = select([units]).where(units.c.code == code_unit)
            return await self.db.fetch_one(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def save(self, db_unit, unit):
        logger.debug("REPOSITORY save unit.")
        try:
            query = self.__upsert(db_unit, unit)
            await self.db.execute(query)
            return await self.find_by_code(unit["code"])
        except Exception as err:
            raise DatabaseException(f"Error on save to database, Contact System Administrator {err}")

    def __upsert(self, db_unit, unit):
        if db_unit is not None:
            return (
                units.update()
                    .values(unit)
                    .where(units.c.code == unit["code"])
            )
        return units.insert().values(unit)


class SubjectsRepository:
    def __init__(self, db):
        self.db: Database = db

    async def find_all(self, active):
        logger.debug("REPOSITORY find all subjects.")
        try:
            query = subjects.select().where(subjects.c.dflag == False)
            query = query.where(subjects.c.active == active) if active != None else query
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_by_code(self, code_subject):
        logger.debug("REPOSITORY find subject by code.")
        try:
            query = select([subjects]).where(subjects.c.code == code_subject)
            return await self.db.fetch_one(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def save(self, db_subject, subject):
        logger.debug("REPOSITORY save subject.")
        try:
            query = self.__upsert(db_subject, subject)
            await self.db.execute(query)
            return await self.find_by_code(subject["code"])
        except Exception as err:
            raise DatabaseException(f"Error on save to database, Contact System Administrator {err}")

    def __upsert(self, db_subject, subject):
        if db_subject is not None:
            return (
                subjects.update()
                    .values(subject)
                    .where(subjects.c.code == subject["code"])
            )
        return subjects.insert().values(subject)
    
    async def deactivate(self, subject):
        logger.debug("REPOSITORY deactivate subject.")
        query = subjects.update().values(active =False, updated_at=datetime.utcnow()).where(subjects.c.code == subject["code"])
        await self.db.execute(query)
        return await self.find_by_code(subject["code"])
