from json import loads

from sanic.response import json
from sanic.blueprints import Blueprint
from schema import Schema, And, Use, SchemaError

from api.doc_api import (
  get_all_subject_api,
  save_subject_api,
  get_subject_by_code_api)

from exceptions import NotFoundException, InvalidRequestException
from models import Assunto
from util.loggers import logger

assuntos_routes = Blueprint("assuntos_v1",
                                 url_prefix="/assuntos",
                                 version="v1")

save_assunto_schema = Schema(
    {
        "name": And(str, Use(str.strip), lambda n: n, error="Name should be a non-empty string"),
        "description": And(str, Use(str.strip), lambda n: n, error="Description should be a non-empty string"),
        "code": And(str, Use(str.strip), lambda n: n, error="Code should be a non-empty string"),
        "active": And(bool, lambda c: c is not None, error="Active should be true or false")
    }
)

@assuntos_routes.get("")
@save_subject_api
async def find_all(request):
  logger.info("Assuntos Get all request.")
  active = None if request.args.get("active") == None else loads(request.args.get("active"))
  assuntos = await request.app.assunto_service.find_all(active=active)
  response = [Assunto(row) for row in assuntos]
  return json(response, status=200)

@assuntos_routes.get("/<code_assunto>")
@get_all_subject_api
async def find_by_code(request, code_assunto):
  logger.info("Assuntos Get by code request.")
  assunto = await request.app.assunto_service.find_by_code(code_assunto=code_assunto)
  if not assunto:
    raise NotFoundException("No Assunto were found matching the given URI.")
  return json(Assunto(assunto))

@assuntos_routes.post("")
@get_subject_by_code_api
async def save(request):
    logger.info("Assuntos Post request.")
    try:
      assunto = request.json
      assunto.update(save_assunto_schema.validate(assunto))
      assunto_response = await request.app.assunto_service.save(assunto)
      return json(Assunto(assunto_response), status=200)
    except SchemaError as e:
      logger.error(f"invalid arguments [{e.args[0]}]")
      raise InvalidRequestException(message=f"{e.args[0]}",category="parameter_not_found")
