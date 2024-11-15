from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


async def init_db():
    CONNECTION_STRING = "mongodb://mongodb:27017"
    client = AsyncIOMotorClient(CONNECTION_STRING)["locations"]
    await init_beanie(database=client, document_models=[])
