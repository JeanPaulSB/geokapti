from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.locations import Locations


async def init_db():
    # TODO: set as env variable
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = AsyncIOMotorClient(CONNECTION_STRING)["locations"]
    await init_beanie(database=client, document_models=[Locations])
