from celery import Celery
from app.utils.haversine import haversine_distance
from app.core.logger import logger

celery_app = Celery(
    "distances", broker="redis://redis:6379/0", backend="redis://redis:6379/0"
)


# Computes the haversine distance between all the locations specified in the request
@celery_app.task()
def compute_total_distance(locations: list):
    logger.info("Starting computation of total distance")
    distance = 0
    for location in range(len(locations) - 1):
        distance += haversine_distance(locations[location], locations[location + 1])
    return {"total_distance": distance}
