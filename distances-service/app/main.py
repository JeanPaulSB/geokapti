from fastapi import FastAPI
from app.api.v1.distances import router
from app.api.health import health_router


app = FastAPI(
    title="Distances microservice",
    description="Microservice REST API for computing distances between locations.",
    version="1.0.0",
    contact={
        "name": "Jean Paul Sierra",
        "url": "https://github.com/JeanPaulSB",
        "email": "jeanpaulsierraboom@gmail.com",
    },
)
app.include_router(router)
app.include_router(health_router)
