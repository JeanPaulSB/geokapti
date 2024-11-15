import celery
import pytest
from app.schemas.location import Location
from app.external_services.celery import compute_total_distance


@pytest.mark.celery(result_backend="redis://localhost:6379/0")
def test_compute_total_distance(celery_app, celery_worker):
    from celery.contrib.testing.tasks import ping

    location1 = {"name": "Jerusalen", "latitude": 50, "longitude": 80}
    location2 = {"name": "LAX", "latitude": 30, "longitude": 20}
    result = compute_total_distance([location1, location2])["total_distance"]
    print(result)
    assert result != 0
