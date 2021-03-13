import asynctest
from asynctest import Mock
from databases import Database

from clients import HttpClient
from services import UnidadeService
from repository import UnidadeRepository


class TestUnidadeService(asynctest.TestCase):
    def setUp(self):
        self.http_client = Mock(HttpClient)
        self.db = asynctest.Mock(Database)
        self.unidade_repository: Mock = asynctest.Mock(UnidadeRepository)
        self.unidade_service = UnidadeService(unidade_repository=self.unidade_repository)


    async def test_find_all_units(self):
        units =[{"name": "Unit One"},
                {"name": "Unit Two"}]
        self.unidade_repository.find_all.return_value = units
        response = await self.unidade_service.find_all(active=None)
        assert response[0]["name"] == units[0]["name"]


    async def test_find_units_by_code(self):
        units = [{"name": "Unit One", "code": "unit_one"},
                 {"name": "Unit Two", "code": "unit_two"}]
        self.unidade_repository.find_by_code.return_value = units
        response = await self.unidade_service.find_by_code("unit_one")
        assert response[0]["code"] == units[0]["code"]


    async def test_save_unit(self):
        unit = {"code": "unit_one", "description": "Unit One",
                "name": "Unit One", "phone": "21 3456-0987",
                "email": "uni_one@gmail.com", "active": True}

        self.unidade_repository.find_by_code.return_value = None
        self.unidade_repository.save.return_value = unit
        unit_response = await self.unidade_service.save(unit)

        assert unit_response["created_at"] != None

        self.unidade_repository.find_by_code.assert_awaited_once_with(unit["code"])
        self.unidade_repository.save.assert_awaited_once_with(None, unit)


    async def test_update_unit(self):
        unit = {"code": "unit_one", "description": "Unit One",
                "name": "Unit One", "phone": "21 3456-0987",
                "email": "uni_one@gmail.com", "active": True}

        db_unit = {"code": "unit_one", "description": "Unit One",
         "name": "Unit One", "phone": "21 3456-0987",
         "email": "uni_one@gmail.com", "active": True}

        self.unidade_repository.find_by_code.return_value = db_unit
        self.unidade_repository.save.return_value = unit
        unit_response = await self.unidade_service.save(unit)

        assert unit_response["updated_at"] != None

        self.unidade_repository.find_by_code.assert_awaited_once_with(unit["code"])
        self.unidade_repository.save.assert_awaited_once_with(db_unit, unit)
