import pytest
import asyncio
import motor
from typing import Generator
from httpx import AsyncClient
from fastapi.testclient import TestClient
from beanie import init_beanie
from app.main import app
from app.models.locations import Locations


async def test_init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/test")
    await init_beanie(database=client["test_db"], document_models=[Locations])
    return client


@pytest.fixture(scope="function")
async def test_client():
    # Create an AsyncClient instance to make requests to the FastAPI api
    async with AsyncClient(
        app=app, base_url="http://test", follow_redirects=True
    ) as ac:
        yield ac


@pytest.fixture(scope="function")
def anyio_backend():
    return "asyncio"


@pytest.fixture(scope="function", autouse=True)
async def initialized_db():
    # Initialize the database and return the client
    client = await test_init_db()
    yield client
    # Teardown - clean up the database after each test
    await client.drop_database("test_db")
    client.close()
