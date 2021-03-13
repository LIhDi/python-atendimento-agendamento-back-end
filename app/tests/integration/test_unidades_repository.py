import asyncio
import pytest

from databases import Database
from sanic.testing import SanicTestClient

from settings import settings
from repository import UnidadeRepository

query_units = "INSERT INTO units(id_int, name, code, email, phone, description, active, dflag, created_at) VALUES (:id_int, :name, :code, :email, :phone, :description, :active, :dflag, :created_at)"

def setup():
    loop = asyncio.get_event_loop()
    db = Database(settings.DB_URL)
    loop.run_until_complete(db.connect())
    loop.run_until_complete(db.execute("delete from appointments"))
    loop.run_until_complete(db.execute("delete from units"))
    loop.run_until_complete(db.disconnect())


