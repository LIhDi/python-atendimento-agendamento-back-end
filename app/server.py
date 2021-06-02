from sanic import Sanic
from databases import Database
from sanic.blueprints import Blueprint
from sanic_openapi import swagger_blueprint
from sanic_limiter import Limiter, get_remote_address
from clients import AwsClient
from settings import settings
from api.infra import infra_routes
from util import context_vars, loggers
from middleware import setup_middlewares
from api.units import units_routes
from api.subjects import subjects_routes
from api.atendimentos import atendimentos_routes
from api.appointments import appointments_routes
from api.schedules import schedules_routes
from exceptions.error_handler import DefaultCustomErrorHandler
from services import UnitsService, SubjectsService, SchedulesService
from services import AuthenticationService, AtendimentoService, AppointmentsService

def setup_rate_limiter(app: Sanic):
    limiter = Limiter(
            app, global_limits=["100/second"], key_func=get_remote_address, strategy="moving-window",
            storage_uri="memory://",
            )

    return limiter


def setup_database(app, db: Database):
    app.db = db

    @app.listener("after_server_start")
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener("after_server_stop")
    async def disconnect_from_db(*args, **kwargs):
        if app.db.is_connected:
            await app.db.disconnect()


def prepare(db: Database = {},
            atendimento_service: AtendimentoService = {},
            authenticator_service: AuthenticationService = {},
            appointments_service: AppointmentsService = {},
            units_service: UnitsService = {},
            subjects_service: SubjectsService = {},
            schedules_service: SchedulesService = {},
            aws_client: AwsClient = {}):

    app = Sanic(__name__)

    app.config.from_object(settings)
    context_vars.application_id_var.set(app.config.APP_ID)

    setup_database(app, db)
    app.atendimento_service = atendimento_service
    app.units_service = units_service
    app.appointments_service = appointments_service
    app.authenticator_service = authenticator_service
    app.subjects_service = subjects_service
    app.schedules_service = schedules_service
    app.aws_client = aws_client


    routes = Blueprint.group(atendimentos_routes,
                             appointments_routes,
                             units_routes,
                             infra_routes,
                             subjects_routes,
                             schedules_routes,
                             url_prefix="/")
    app.blueprint(routes)
    app.blueprint(swagger_blueprint)

    app.error_handler = DefaultCustomErrorHandler()
    setup_middlewares(app)
    loggers.setup_logger()

    return app
