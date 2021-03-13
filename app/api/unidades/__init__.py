from json import loads

from sanic.response import json
from sanic.blueprints import Blueprint
from schema import Schema, And, Use, SchemaError

from api.doc_api import (
  get_all_unit_api,
  save_unit_api,
  get_unit_by_code_api)

from exceptions import NotFoundException, InvalidRequestException
from models import Unidade
from util.loggers import logger

unidades_routes = Blueprint("unidades_v1",
                                 url_prefix="/unidades",
                                 version="v1")

save_unidade_schema = Schema(
    {
        "name": And(str, Use(str.strip), lambda n: n, error="Name should be a non-empty string"),
        "email": And(str, Use(str.strip), lambda n: n, error="Email should be a non-empty string"),
        "phone": And(str, Use(str.strip), lambda n: n, error="Phone should be a non-empty string"),
        "description": And(str, Use(str.strip), lambda n: n, error="Description should be a non-empty string"),
        "code": And(str, Use(str.strip), lambda n: n, error="Code should be a non-empty string"),
        "active": And(bool, lambda c: c is not None, error="Active should be true or false")
    }
)

@unidades_routes.get("")
@get_all_unit_api
async def find_all(request):
  logger.info("Unidades Get all request.")
  active = None if request.args.get("active") == None else loads(request.args.get("active"))
  unidades = await request.app.unidade_service.find_all(active=active)
  response = [Unidade(row) for row in unidades]
  return json(response, status=200)

@unidades_routes.get("/<code_unidade>")
@get_unit_by_code_api
async def find_by_code(request, code_unidade):
  logger.info("Unidades Get by code request.")
  unidade = await request.app.unidade_service.find_by_code(code_unidade=code_unidade)
  if not unidade:
    raise NotFoundException("No Unidade were found matching the given URI.")
  return json(Unidade(unidade))

@unidades_routes.post("")
@save_unit_api
async def save(request):
    logger.info("Unidades Post request.")
    try:
      unidade = request.json
      unidade.update(save_unidade_schema.validate(unidade))
      unidade_response = await request.app.unidade_service.save(unidade)
      return json(Unidade(unidade_response), status=200)
    except SchemaError as e:
      logger.error(f"invalid arguments [{e.args[0]}]")
      raise InvalidRequestException(message=f"{e.args[0]}",category="parameter_not_found")
