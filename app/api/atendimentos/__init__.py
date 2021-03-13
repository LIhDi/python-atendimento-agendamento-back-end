from sanic.response import json
from sanic.blueprints import Blueprint

from util.loggers import logger

atendimentos_routes = Blueprint("atendimentos_v1",
                                 url_prefix="/atendimentos",
                                 version="v1")


@atendimentos_routes.get("")
async def find_all(request):
  logger.info("Atendimentos Get all request.")
  return json(200)

