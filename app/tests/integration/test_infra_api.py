import pytest
from sanic.testing import SanicTestClient


@pytest.mark.IT
async def test_sanic_status_endpoint(test_cli: SanicTestClient):
    response = await test_cli.get("/v1/status/ping")
    assert response.status == 200
    json_response = await response.json()
    assert json_response["pong"]


@pytest.mark.IT
async def test_health_check_success(test_cli: SanicTestClient):
    response = await test_cli.get("/v1/status/healthcheck")
    expected_response = {
        "dependencies": [
            {"isCritical": True, "name": "MySQL", "status": "UP"}
        ],
        "message": "All dependencies are up",
        "status": "UP",
    }

    assert response.status == 200
    assert await response.json() == expected_response


@pytest.mark.IT
async def test_critical_service_fail(test_cli: SanicTestClient):
    await test_cli.app.db.disconnect()

    response = await test_cli.get("/v1/status/healthcheck")
    expected_response = {
        "dependencies": [
            {"detail": "DatabaseBackend is not running", "isCritical": True, "name": "MySQL", "status": "DOWN"}
        ],
        "message": "All dependencies are down",
        "status": "DOWN",
    }

    assert response.status == 404
    assert await response.json() == expected_response

