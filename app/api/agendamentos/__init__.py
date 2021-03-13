from sanic.response import json
from sanic.blueprints import Blueprint

from exceptions import NotFoundException, InvalidRequestException
from models import Appointment, Status
from util.loggers import logger

agendamentos_routes = Blueprint("agendamentos_v1",
                                 url_prefix="/agendamentos",
                                 version="v1")


@agendamentos_routes.get("")
async def find_all(request):
  logger.info("Appointments Get all request.")
  agendamentos = await request.app.agendamento_service.find_all()
  return json(agendamentos, status=200)

@agendamentos_routes.get("/<national_registration>")
async def find_by_status(request, national_registration):
  logger.info("Appointments Get by status request.")
  person = await request.app.pessoa_service.find_by_national_registration(national_registration=national_registration)
  if not person:
    raise NotFoundException("No Person were found matching the given URI.")
  status_code = request.args.get("status", None)
  if not status_code:
    raise InvalidRequestException("Query parameter status is required!",
                                  category="required_param_not_present")
  status_code = await request.app.agendamento_service.find_status_by_code(status_code=status_code)
  agendamentos = await request.app.agendamento_service.find_by_status(status_code=status_code,
                                                                      national_registration=national_registration)
  response = [Appointment(row) for row in agendamentos]
  return json(response, status=200)

@agendamentos_routes.get("/status")
async def find_all_status(request):
  logger.info("Appointments Get all status request.")
  status = await request.app.agendamento_service.find_all_status()
  response = [Status(row) for row in status]
  return json(response, status=200)

