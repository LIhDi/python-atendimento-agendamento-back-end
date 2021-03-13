import asynctest
from databases import Database
from exceptions import DatabaseException
from repository import UnidadeRepository


class TestUnidadeRepository(asynctest.TestCase):
    def setUp(self):
        self.db = asynctest.Mock(Database)
        self.unidade_repository = UnidadeRepository(db=self.db)

    async def test_find_all_fails_when_db_error_occurs(self):
        self.db.fetch_all.side_effect = Exception
        with self.assertRaises(DatabaseException):
            await self.unidade_repository.find_all(active=True)

    async def test_find_by_code_fails_when_db_error_occurs(self):
        self.db.fetch_one.side_effect = Exception
        with self.assertRaises(DatabaseException):
            await self.unidade_repository.find_by_code(code_unidade="code_one")

    async def test_save_fails_when_db_error_occurs(self):
        self.db.execute.side_effect = Exception
        with self.assertRaises(DatabaseException):
            await self.unidade_repository.save({}, {})