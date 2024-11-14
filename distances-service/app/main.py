from fastapi import FastAPI
from contextlib import asynccontextmanager
from .core.database import init_db
from .api.v1.distances import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO: log info
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Running distances microservice"}
