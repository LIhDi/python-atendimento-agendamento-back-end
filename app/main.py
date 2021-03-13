import server

from databases import Database
from settings import settings
from clients import AwsClient, HttpClient
from repository import AtendimentoRepository, AgendamentoRepository, UnidadeRepository, AssuntoRepository, \
  PessoaRepository
from services import AuthenticationService, AtendimentoService, AgendamentoService, UnidadeService, AssuntoService, \
  PessoaService

db = Database(settings.DB_URL)
aws_client = AwsClient(settings)

http_client = HttpClient(settings)
authenticator_service = AuthenticationService(http_client, settings)

atendimento_repository = AtendimentoRepository(db=db)
atendimento_service = AtendimentoService(http_client,
                                            settings,
                                            atendimento_repository,
                                            aws_client)

agendamento_repository = AgendamentoRepository(db=db)
agendamento_service = AgendamentoService(agendamento_repository)

unidade_repository = UnidadeRepository(db=db)
unidade_service = UnidadeService(unidade_repository)

assunto_repository = AssuntoRepository(db=db)
assunto_service = AssuntoService(assunto_repository)

pessoa_repository = PessoaRepository(db=db)
pessoa_service = PessoaService(pessoa_repository)

app = server.prepare(db=db,
                     authenticator_service=authenticator_service,
                     aws_client=aws_client,
                     atendimento_service=atendimento_service,
                     unidade_service=unidade_service,
                     agendamento_service=agendamento_service,
                     assunto_service=assunto_service,
                     pessoa_service=pessoa_service
                     )


app.run(
    host=app.config.HOST,
    port=app.config.PORT,
    debug=app.config.DEBUG,
    auto_reload=app.config.DEBUG,
    access_log=app.config.ACCESS_LOG
)
