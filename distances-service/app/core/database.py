from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie


async def init_db():
    CONNECTION_STRING = ""
    client = AsyncIOMotorClient(CONNECTION_STRING)
    await init_beanie(database=client, document_models=[])
