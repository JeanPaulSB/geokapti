import pytest
from app.models.locations import Locations
from app.schemas.location import LocationUpdate
from bson import ObjectId
from httpx import AsyncClient
from pydantic import ValidationError


# Helper function to populate db
async def create_location(name: str, latitude: float, longitude: float) -> Locations:
    location = Locations(name=name, latitude=latitude, longitude=longitude)
    await location.save()
    return location


@pytest.mark.anyio
async def test_create_location_with_valid_coordinates(
    test_client, initialized_db
) -> None:
    # Arrange
    location = {"name": "JPL Lab", "latitude": 40, "longitude": 20}
    # Act
    response = await test_client.post("/locations", json=location)
    # Assert
    assert response.status_code == 201


@pytest.mark.anyio
async def test_create_location_with_invalid_coordinates(
    test_client, initialized_db
) -> None:
    # Arrange
    location = {"name": "Narnia", "latitude": 40, "longitude": 200}
    # Act
    response = await test_client.post("/locations", json=location)
    # Assert
    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_location(test_client, initialized_db) -> None:
    # Arrange
    location = await create_location("random_location", 40, 20)
    # Act
    response = await test_client.get(f"/locations/{str(location.id)}")
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert data["name"] == "random_location"
    assert data["latitude"] == 40
    assert data["longitude"] == 20


@pytest.mark.anyio
async def test_get_location_with_invalid_id(test_client, initialized_db) -> None:

    # Arrange
    random_id = "6736111bab0d0a06f5fa436"
    # Act
    response = await test_client.get(f"/locations/{random_id}")
    # Assert
    assert response.status_code == 404


@pytest.mark.anyio
async def test_get_locations(test_client, initialized_db) -> None:
    # Arrange
    locations = [
        await create_location("random_location", i * 2, i * 2) for i in range(10)
    ]
    # Act
    response = await test_client.get("/locations")
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert len(data) == 10


@pytest.mark.anyio
async def test_update_location(test_client, initialized_db) -> None:
    # Arrange
    location = await create_location("location", 4, 5)
    location_data = LocationUpdate(name="Athenas", latitude=40, longitude=20)
    # Act
    response = await test_client.put(
        f"/locations/{location.id}", json=location_data.dict()
    )
    data = response.json()
    # Arrange
    assert response.status_code == 200
    assert data["name"] == "Athenas"
    assert data["latitude"] == 40
    assert data["longitude"] == 20


@pytest.mark.anyio
async def test_update_location_with_invalid_id(test_client, initialized_db) -> None:
    # Arrange
    random_id = "6736111bab0d0a06f5fa436"
    location_data = LocationUpdate(name="Athenas", latitude=40, longitude=20)
    # Act
    response = await test_client.put(
        f"/locations/{random_id}", json=location_data.dict()
    )
    # Arrange
    assert response.status_code == 404


@pytest.mark.anyio
async def test_update_location_with_invalid_coordinates(
    test_client, initialized_db
) -> None:
    # Arrange
    location = await create_location("location", 4, 5)

    with pytest.raises(ValidationError):
        location_data = LocationUpdate(name="Athenas", latitude=80, longitude=450.0)
        # Act
        response = await test_client.put(
            f"/locations/{location.id}", json=location_data.dict()
        )
        # Arrange
        assert response.status_code == 422



@pytest.mark.anyio
async def test_delete_location(test_client, initialized_db) -> None:
    # Arrange
    location = await create_location("location", 4, 5)
    # Act
    response = await test_client.delete(f"/locations/{location.id}")
    # Assert
    assert response.status_code == 204
