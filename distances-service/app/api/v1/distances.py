import httpx
from fastapi import APIRouter
from typing import List
from app.schemas.locations import Locations
from app.external_services.location import fetch_locations
from celery.result import AsyncResult
from app.external_services.celery import celery_app
from app.external_services.celery import compute_total_distance
from app.schemas.task import Task
from app.schemas.distance import TotalDistanceResult
from app.core.logger import logger

router = APIRouter(tags=["distances"])


# adds computation to the queue
@router.post(
    "/",
    description="Receives a list of locations, then starts the computation of the total distance between them by creating a task"
    "and finally returns the id of the created task. You must use this id to query the status of the task and its result.",
    response_model=Task,
)
async def compute_distance(locations: Locations) -> Task:
    result = await fetch_locations(locations.ids)
    logger.info("Computing total distance")
    task = compute_total_distance.delay(result)
    return Task(id=task.id, status=task.status)


# retrieves the result of the computation
@router.get(
    "/{task_id}",
    description="Recieves the id of the task, then delivers its result if the task is already completed.",
    response_model=TotalDistanceResult,
)
async def get_total_distance(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    if result.successful():
        logger.info("Task successfully completed")
        return TotalDistanceResult(total_distance=result.result["distance"])
