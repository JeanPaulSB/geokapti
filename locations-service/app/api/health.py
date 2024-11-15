from fastapi import APIRouter
from app.core.logger import logger

health_router = APIRouter( tags=["health"])


@health_router.get("/health", status_code=204)
async def health():
    """
    Health check to ensure that the app is up and running without problems.
    """
    logger.info("Up and running!")
