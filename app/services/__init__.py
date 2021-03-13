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


class AgendamentoService:
    def __init__(self, agendamento_repository):
        self.agendamento_repository = agendamento_repository

    async def find_all(self):
        logger.debug("SERVICE find all appointments.")
        return await self.agendamento_repository.find_all()

    async def find_by_status(self, status_code, national_registration):
        logger.debug(f"SERVICE find appointments by status - {status_code}.")
        return await self.agendamento_repository.find_by_status(status_code, national_registration)

    async def find_status_by_code(self, status_code):
        logger.debug(f"SERVICE find status by code - {status_code}.")
        db_status = await self.agendamento_repository.find_status_by_code(status_code)
        if not db_status:
            raise NotAcceptableException(
                f"Appointment status is invalid. There is no status for - {status_code}.")
        return status_code

    async def find_all_status(self):
        logger.debug("SERVICE find all status.")
        return await self.agendamento_repository.find_all_status()


class UnidadeService:
    def __init__(self, unidade_repository):
        self.unidade_repository = unidade_repository

    async def find_all(self, active):
        logger.debug("SERVICE find all unidades.")
        return await self.unidade_repository.find_all(active)

    async def find_by_code(self, code_unidade):
        logger.debug("SERVICE find unidade by code.")
        return await self.unidade_repository.find_by_code(code_unidade)

    async def save(self, unidade):
        logger.debug("SERVICE save unidade.")
        db_unidade = await self.unidade_repository.find_by_code(unidade["code"])
        dates = self.dates_to_update(db_unidade)
        unidade.update(dates)
        unidade = await self.unidade_repository.save(db_unidade, unidade)
        return unidade

    def dates_to_update(self, db_unidade):
        if db_unidade is not None:
            dates = {"updated_at": datetime.utcnow()}
        else:
            dates = {"created_at": datetime.utcnow(), "dflag": False}
        return dates


class AssuntoService:
    def __init__(self, assunto_repository):
        self.assunto_repository = assunto_repository

    async def find_all(self, active ):
        logger.debug("SERVICE find all assuntos.")
        return await self.assunto_repository.find_all(active)

    async def find_by_code(self, code_assunto):
        logger.debug("SERVICE find assuntos by code.")
        return await self.assunto_repository.find_by_code(code_assunto)

    async def save(self, assunto):
        logger.debug("SERVICE save assunto.")
        db_assunto = await self.assunto_repository.find_by_code(assunto["code"])
        dates = self.dates_to_update(db_assunto)
        assunto.update(dates)
        assunto = await self.assunto_repository.save(db_assunto, assunto)
        return assunto

    def dates_to_update(self, db_assunto):
        if db_assunto is not None:
            dates = {"updated_at": datetime.utcnow()}
        else:
            dates = {"created_at": datetime.utcnow(), "dflag": False}
        return dates


class PessoaService:
    def __init__(self, pessoa_repository):
        self.pessoa_repository = pessoa_repository

    async def find_by_national_registration(self, national_registration):
        logger.debug("SERVICE find by national registration.")
        return await self.pessoa_repository.find_by_national_registration(national_registration)