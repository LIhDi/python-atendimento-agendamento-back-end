from datetime import datetime
from exceptions import NotAcceptableException
from util.loggers import logger


class AuthenticationService:
    def __init__(self, http_client, config):
        self.http_client = http_client
        self.validation_url = config.VALIDATION_TOKEN_API_URL + config.TOKEN_INFORMATION

    async def authenticate(self, token):
        logger.debug("SERVICE authenticate.")
        if await self.token_validate(token):
            return True
        else:
            return False

    async def token_validate(self, token):
        logger.debug("SERVICE token validate.")
        params = {"token": token.replace("-", "")}
        url = self.validation_url
        for key, value in params.items():
            url = url.replace(f"<{key}>", f"{value}")
        response = await self.http_client.get(url)
        if response["status"] == 200:
            return True
        else:
            logger.error(f"VALIDATOR url: {url} status code: {response['status']}")
            return False


class AtendimentoService:
    def __init__(self, http_client, config, atendimento_repository, aws_client):
        self.http_client = http_client
        self.atendimento_repository = atendimento_repository


class AppointmentsService:
    def __init__(self, appointments_repository):
        self.appointments_repository = appointments_repository

    async def find_all(self):
        logger.debug("SERVICE find all appointments.")
        return await self.appointments_repository.find_all()

    async def find_by_id(self, appointment_id):
        logger.debug("SERVICE find appointment by id.")
        return await self.appointments_repository.find_by_id(appointment_id)

    async def find_by_status(self, status_code, national_registration):
        logger.debug(f"SERVICE find appointments by status - {status_code}.")
        return await self.appointments_repository.find_by_status(status_code, national_registration)

    async def find_status_by_code(self, status_code):
        logger.debug(f"SERVICE find status by code - {status_code}.")
        db_status = await self.appointments_repository.find_status_by_code(status_code)
        if not db_status:
            raise NotAcceptableException(
                f"Appointment status is invalid. There is no status for - {status_code}.")
        return status_code

    async def find_all_status(self):
        logger.debug("SERVICE find all status.")
        return await self.appointments_repository.find_all_status()
    
    async def cancel(self, appointment_id):
        logger.debug("SERVICE appointment cancelation.")
        return await self.appointments_repository.cancel(appointment_id)
    
    async def save(self, appointment):
        logger.debug("SERVICE save appointment.")
        dates = self.dates_to_update(db_unit)
        appointment.update(dates)
        appointment = await self.appointments_repository.save(unit)
        return appointment

    def dates_to_update(self, appointment):
        if appointment is not None:
            dates = {"updated_at": datetime.utcnow()}
        else:
            dates = {"created_at": datetime.utcnow(), "dflag": False}
        return dates


class UnitsService:
    def __init__(self, units_repository):
        self.units_repository = units_repository

    async def find_all(self, active):
        logger.debug("SERVICE find all units.")
        return await self.units_repository.find_all(active)

    async def find_by_code(self, code_unit):
        logger.debug("SERVICE find unit by code.")
        return await self.units_repository.find_by_code(code_unit)

    async def save(self, unit):
        logger.debug("SERVICE save unit.")
        db_unit = await self.units_repository.find_by_code(unit["code"])
        dates = self.dates_to_update(db_unit)
        unit.update(dates)
        unit = await self.units_repository.save(db_unit, unit)
        return unit

    def dates_to_update(self, db_unit):
        if db_unit is not None:
            dates = {"updated_at": datetime.utcnow()}
        else:
            dates = {"created_at": datetime.utcnow(), "dflag": False}
        return dates


class SubjectsService:
    def __init__(self, subjects_repository):
        self.subjects_repository = subjects_repository

    async def find_all(self, active ):
        logger.debug("SERVICE find all subjects.")
        return await self.subjects_repository.find_all(active)

    async def find_by_code(self, code_subject):
        logger.debug("SERVICE find subjects by code.")
        return await self.subjects_repository.find_by_code(code_subject)

    async def save(self, subject):
        logger.debug("SERVICE save subject.")
        db_subject = await self.subjects_repository.find_by_code(subject["code"])
        dates = self.dates_to_update(db_subject)
        subject.update(dates)
        subject = await self.subjects_repository.save(db_subject, subject)
        return subject

    def dates_to_update(self, db_subject):
        if db_subject is not None:
            dates = {"updated_at": datetime.utcnow()}
        else:
            dates = {"created_at": datetime.utcnow(), "dflag": False}
        return dates
    
    async def deactivate(self, subject):
        logger.debug("SERVICE deactivate subject.")
        subject = await self.subjects_repository.deactivate(subject)
        return subject

class SchedulesService:
    def __init__(self, schedules_repository):
        self.schedules_repository = schedules_repository

    async def find_all(self, status):
        logger.debug("SERVICE find all schedules.")
        return await self.schedules_repository.find_all(status) 

    async def save(self, schedules):
        logger.debug("SERVICE save schedules.")
        for schedule in schedules:
            schedule_status = self.schedules_repository.find_status_by_code(schedule["code"])
            schedule["id_schedule_status"] = schedule_status["id_int"]
            logger.debug(schedule)
            await self.schedules_repository.save(schedule)
        return schedules
