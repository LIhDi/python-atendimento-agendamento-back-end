import uuid

from asynctest import TestCase, Mock
from faker import Faker

from clients import HttpClient
from services import AuthenticationService


class AuthenticationServiceTest(TestCase):
    def setUp(self):
        self.http_client = Mock(HttpClient)
        self.config = Mock()
        self.config.VALIDATION_TOKEN_API_URL = ""
        self.config.TOKEN_INFORMATION = "/<token>"
        self.validator_service = AuthenticationService(self.http_client, self.config)

    async def test_authenticate(self):
        token = str(uuid.uuid4()).replace("-", "")
        expected_url_call = f"/{token}"
        response = {"status": 200}
        self.http_client.get.return_value = response

        assert await self.validator_service.authenticate(token) is True

        self.http_client.get.assert_awaited_once_with(expected_url_call)


    async def test_authenticate_when_token_not_exists(self):
        token = str(uuid.uuid4()).replace("-", "")
        expected_url_call = f"/{token}"
        response = {"status": 404}
        self.http_client.get.return_value = response

        assert await self.validator_service.authenticate(token) is False

        self.http_client.get.assert_awaited_once_with(expected_url_call)

