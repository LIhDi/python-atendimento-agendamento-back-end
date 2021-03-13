from util.loggers import logger
from sanic.blueprints import Blueprint
from sanic.response import json
from sanic_openapi import doc

infra_routes = Blueprint("infra_v1",
                         url_prefix="/status",
                         version="v1")


@infra_routes.get("/ping")
@doc.summary("Ping status API")
@doc.produces({"pong": str})
async def ping(request):
    logger.debug("Serving PING request.")
    return json({"pong": True})


@infra_routes.get("/healthcheck")
@doc.summary("Healthcheck status API")
async def healthcheck(request):
    data = {
        "status": "UP",
        "message": "All dependencies are up",
        "dependencies": {
            "mysql": {
                "name": "MySQL",
                "isCritical": True,
                "status": "DOWN"
                }
            },
    }

    http_status = 200

    checks = [await _db_check(request.app.db)]

    for check in checks:
        data["dependencies"].update(check)

    data["dependencies"] = list(data["dependencies"].values())

    if any(s["status"] == "DOWN" for s in data["dependencies"]):
        data["status"] = "PARTIAL"
        data["message"] = "Some dependencies are down"

    if any(s["status"] == "DOWN" and s["isCritical"] for s in data["dependencies"]):
        data["status"] = "DOWN"
        data["message"] = "Critical dependencies are down"
        http_status = 404

    if all(s["status"] == "DOWN" for s in data["dependencies"]):
        data["message"] = "All dependencies are down"

    logger.debug(
        "Healthcheck request served. Status: "
        f'[mysql:{data["dependencies"][0]["status"]}|'
        f'{data["dependencies"][0].get("detail")}] '
        f'[general:{data["status"]}|{data["message"]}]'
    )

    return json(data, http_status)


async def _db_check(db):
    try:
        row = await db.fetch_one("SELECT 1")
        if row[0] != 1:
            raise Exception("MySQL return error")
        return {
            "mysql": {
                "name": "MySQL",
                "isCritical": True,
                "status": "UP"
                }
            }
    except Exception as e:
        return {
            "mysql": {
                "name": "MySQL",
                "isCritical": True,
                "status": "DOWN",
                "detail": str(e)
                }
            }

