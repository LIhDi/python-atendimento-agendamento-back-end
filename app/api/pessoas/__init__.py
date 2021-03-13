from sanic.response import json
from sanic.blueprints import Blueprint

from exceptions import NotFoundException
from models import Person
from util.loggers import logger

pessoas_routes = Blueprint("pessoas_v1",
                                 url_prefix="/pessoas",
                                 version="v1")


@pessoas_routes.get("/<national_registration>")
async def find_by_national_registration(request, national_registration):
  logger.info("Persons Get by national registration request.")
  person = await request.app.pessoa_service.find_by_national_registration(national_registration=national_registration)
  if not person:
    raise NotFoundException("No Person were found matching the given URI.")
  return json(Person(person), status=200)

