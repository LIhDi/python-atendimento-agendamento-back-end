import pytest
import asyncio
import logging

from os import path as os_path
from sys import path as sys_path
from databases import Database



sys_path.insert(0, os_path.join(os_path.dirname(os_path.abspath(__file__)), ".."))
from tests.data import units_list
from server import prepare
from settings import settings
from clients import HttpClient, AwsClient
from repository import AtendimentoRepository, UnidadeRepository
from services import AuthenticationService, AtendimentoService, UnidadeService


@pytest.fixture
def sanic_app():
    app = prepare()
    return app


@pytest.fixture
def logger():
    logger = logging.getLogger(__name__)
    numeric_level = getattr(logging, "INFO", None)
    logger.setLevel(numeric_level)
    return logger


@pytest.fixture
def test_db():
    units = units_list()
    return {
        "units": units,
    }


@pytest.fixture
def units(test_db):
    return test_db["units"]


@pytest.fixture
def authentication_service():
    return AuthenticationService(HttpClient(settings), settings)


@pytest.fixture
def aws_client():
    return AwsClient(settings)


@pytest.fixture
def db():
    return Database(settings.DB_URL)


@pytest.fixture
def connected_db(db):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.connect())
    return db


@pytest.fixture
def unidade_repository(db):
    return UnidadeRepository(db)


@pytest.fixture
def unidade_service(unidade_repository):
    return UnidadeService(unidade_repository)


@pytest.fixture
def atendimento_repository(db):
    return AtendimentoRepository(db)


@pytest.fixture
def atendimento_service(atendimento_repository, aws_client):
    return AtendimentoService(HttpClient(settings),
                                settings,
                                atendimento_repository,
                                aws_client)


@pytest.fixture
def test_cli(loop, sanic_app, sanic_client,
             atendimento_service,
             authentication_service, db):

    sanic_app.db = db
    sanic_app.atendimento_service = atendimento_service
    sanic_app.authenticator_service = authentication_service
    sanic_app.aws_client = AwsClient(settings)

    yield loop.run_until_complete(sanic_client(sanic_app))









