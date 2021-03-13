from databases import Database
from sqlalchemy.sql import select
from exceptions import DatabaseException
from util.loggers import logger
from tables import status, appointments, units, subjects, persons


class AtendimentoRepository:
    def __init__(self, db):
        self.db: Database = db


class AgendamentoRepository:
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
            join = appointments.join(status)
            query = (
                select([appointments])
                    .select_from(join)
                    .where(appointments.c.national_registration == national_registration)
                    .where(status.c.code == status_code))
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_status_by_code(self, status_code):
        logger.debug("REPOSITORY find status by code.")
        try:
            query = (
                select([status])
                .where(status.c.code == status_code)
                .where(status.c.dflag == False))
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_all_status(self):
        logger.debug("REPOSITORY find all status.")
        try:
            query = select([status]).where(status.c.dflag == False)
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")


class UnidadeRepository:
    def __init__(self, db):
        self.db: Database = db

    async def find_all(self, active):
        logger.debug("REPOSITORY find all unidades.")
        try:
            query = units.select().where(units.c.dflag == False)
            query = query.where(units.c.active == active) if active != None else query
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_by_code(self, code_unidade):
        logger.debug("REPOSITORY find unidade by code.")
        try:
            query = select([units]).where(units.c.code == code_unidade)
            return await self.db.fetch_one(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def save(self, db_unidade, unidade):
        logger.debug("REPOSITORY save unidade.")
        try:
            query = self.__upsert(db_unidade, unidade)
            await self.db.execute(query)
            return await self.find_by_code(unidade["code"])
        except Exception as err:
            raise DatabaseException(f"Error on save to database, Contact System Administrator {err}")

    def __upsert(self, db_unidade, unidade):
        if db_unidade is not None:
            return (
                units.update()
                    .values(unidade)
                    .where(units.c.code == unidade["code"])
            )
        return units.insert().values(unidade)


class AssuntoRepository:
    def __init__(self, db):
        self.db: Database = db

    async def find_all(self, active):
        logger.debug("REPOSITORY find all assuntos.")
        try:
            query = subjects.select().where(subjects.c.dflag == False)
            query = query.where(subjects.c.active == active) if active != None else query
            return await self.db.fetch_all(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def find_by_code(self, code_assunto):
        logger.debug("REPOSITORY find assunto by code.")
        try:
            query = select([subjects]).where(subjects.c.code == code_assunto)
            return await self.db.fetch_one(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")

    async def save(self, db_assunto, assunto):
        logger.debug("REPOSITORY save assunto.")
        try:
            query = self.__upsert(db_assunto, assunto)
            await self.db.execute(query)
            return await self.find_by_code(assunto["code"])
        except Exception as err:
            raise DatabaseException(f"Error on save to database, Contact System Administrator {err}")

    def __upsert(self, db_assunto, assunto):
        if db_assunto is not None:
            return (
                subjects.update()
                    .values(assunto)
                    .where(subjects.c.code == assunto["code"])
            )
        return subjects.insert().values(assunto)


class PessoaRepository:
    def __init__(self, db):
        self.db: Database = db

    async def find_by_national_registration(self, national_registration):
        logger.debug("REPOSITORY find person by national registration.")
        try:
            query = select([persons]).where(persons.c.national_registration == national_registration)
            return await self.db.fetch_one(query)
        except Exception as err:
            raise DatabaseException(f"Error on fetch database, Contact System Administrator {err}")
