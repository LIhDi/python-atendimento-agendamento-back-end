import server

from databases import Database
from settings import settings
from clients import AwsClient, HttpClient
from repository import AtendimentoRepository, AppointmentsRepository
from repository import UnitsRepository, SubjectsRepository
from repository.schedules import SchedulesRepository
from services import AppointmentsService, UnitsService, SubjectsService
from services import AuthenticationService, AtendimentoService, SchedulesService

db = Database(settings.DB_URL)
aws_client = AwsClient(settings)

http_client = HttpClient(settings)
authenticator_service = AuthenticationService(http_client, settings)

atendimento_repository = AtendimentoRepository(db=db)
atendimento_service = AtendimentoService(http_client,
                                            settings,
                                            atendimento_repository,
                                            aws_client)

appointments_repository = AppointmentsRepository(db=db)
appointments_service = AppointmentsService(appointments_repository)

schedules_repository = SchedulesRepository(db=db)
schedules_service = SchedulesService(schedules_repository)

units_repository = UnitsRepository(db=db)
units_service = UnitsService(units_repository)

subjects_repository = SubjectsRepository(db=db)
subjects_service = SubjectsService(subjects_repository)

app = server.prepare(db=db,
                     authenticator_service=authenticator_service,
                     aws_client=aws_client,
                     atendimento_service=atendimento_service,
                     units_service=units_service,
                     appointments_service=appointments_service,
                     subjects_service=subjects_service,
                     schedules_service=schedules_service
                     )


app.run(
    host=app.config.HOST,
    port=app.config.PORT,
    debug=app.config.DEBUG,
    auto_reload=app.config.DEBUG,
    access_log=app.config.ACCESS_LOG
)
