import json
import asynctest
from typing import Any
from databases import Database

from api.infra import healthcheck
from clients import AwsClient


class TestHealthCheckApi(asynctest.TestCase):
    def setUp(self):
        self.request = asynctest.Mock(Any)
        self.request.app = asynctest.Mock(Any)
        self.request.app.db = asynctest.Mock(Database)
        self.request.app.aws_client = asynctest.Mock(AwsClient)


    async def test_check_health_with_all_services_are_down(self):
        self.request.app.db.fetch_one.side_effect = Exception("DatabaseBackend is not running")
        expected_response = {
            "dependencies": [
                {"detail": "DatabaseBackend is not running", "isCritical": True, "name": "MySQL", "status": "DOWN"}
                ],
            "message": "All dependencies are down",
            "status": "DOWN",
        }
        response = await healthcheck(self.request)
        assert response.status == 404

        assert json.loads(response.body) == expected_response


    async def test_check_health_with_no_critical_service_is_down(self):
        self.request.app.db.fetch_one.return_value = [1]
        expected_response = {
            "dependencies": [
                {"isCritical": True, "name": "MySQL", "status": "UP"},
            ],
            "message": "All dependencies are up",
            "status": "UP",
        }
        response = await healthcheck(self.request)

        assert json.loads(response.body) == expected_response
        assert response.status == 200
