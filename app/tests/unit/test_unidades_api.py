import pytest
import asynctest
from json import dumps
from databases import Database
from sanic.testing import SanicTestClient

from services import UnidadeService


@pytest.fixture
def test_cli_mock(loop, sanic_app, sanic_client):
    sanic_app.unidade_service = asynctest.Mock(UnidadeService)
    sanic_app.db = asynctest.Mock(Database)
    sanic_app.db.is_connected = True
    return loop.run_until_complete(sanic_client(sanic_app))


async def test_save_unidade_when_requested_params_not_sent(test_cli_mock):
    data = {
        "name":"Teste",
        "description":"Descrição Teste",
        "active": True,
        "phone": "21 9999-0000",
        "email": "teste@gmail.com"
        }
    data_json = dumps(data)
    response = await test_cli_mock.post("/v1/unidades", data=data_json)
    response_data = await response.json()
    expected_response = {
        "error": {
            "status_code": 400,
            "status": "Bad Request",
            "message": "Missing key: 'code'",
            "type": "invalid_request_error",
            "category": "parameter_not_found",
        }
    }

    assert response.status == 400
    assert response_data == expected_response


async def test_save_unidade_with_success(test_cli_mock: SanicTestClient):
    data = {
        "name": "Teste",
        "description": "Descrição Teste",
        "active": True,
        "phone": "21 9999-0000",
        "email": "teste@gmail.com",
        "code": "code_teste"
        }
    data_json = dumps(data)
    test_cli_mock.app.unidade_service.save.return_value = data
    response = await test_cli_mock.post("/v1/unidades", data=data_json)

    assert response.status == 200


async def test_find_by_code_fails_when_unidade_code_not_found(test_cli_mock):
    code = "unidade_teste"
    test_cli_mock.app.unidade_service.find_by_code.return_value = {}
    response = await test_cli_mock.get(f"/v1/unidades/{code}")
    assert response.status == 404
    response_data = await response.json()
    expected_response = {
        "error": {
            "status_code": 404,
            "status": "Not Found",
            "message": "No Unidade were found matching the given URI.",
            "type": "invalid_request_error",
            "category": "resource_not_found",
            }
        }

    assert response.status == 404
    assert response_data == expected_response


async def test_find_by_code_with_success(test_cli_mock):
    data = {
        "name": "Teste",
        "description": "Descrição Teste",
        "active": True,
        "phone": "21 9999-0000",
        "email": "teste@gmail.com",
        "code": "code_teste"
        }
    test_cli_mock.app.unidade_service.find_by_code.return_value = data
    response = await test_cli_mock.get(f"/v1/unidades/{data['code']}")
    assert response.status == 200


async def test_find_all_when_unidade_is_emty(test_cli_mock):
    test_cli_mock.app.unidade_service.find_all.return_value = []
    response = await test_cli_mock.get("/v1/unidades")
    assert response.status == 200


async def test_find_all_unidade_with_success(test_cli_mock):
    data = [{
        "name": "Teste",
        "description": "Descrição Teste",
        "active": True,
        "phone": "21 9999-0000",
        "email": "teste@gmail.com",
        "code": "code_teste",
        }]
    test_cli_mock.app.unidade_service.find_all.return_value = data
    response = await test_cli_mock.get("/v1/unidades")
    assert response.status == 200

