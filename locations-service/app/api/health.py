from fastapi import APIRouter
from app.core.logger import logger

health_router = APIRouter(prefix="/health", tags=["health"])

@health_router.get("/",status_code=204)
async def health():
    logger.info("Up and running!")