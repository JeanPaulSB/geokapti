import pytest
from app.utils.haversine import haversine_distance


def test_haversine_distance_between_same_location():
    # Arrange
    location1 = {"latitude": 50, "longitude": 50}
    location2 = {"latitude": 50, "longitude": 50}
    # Act
    distance = haversine_distance(location1, location2)
    # Assert
    assert distance == 0


def test_haversine_distance_same_meridian():
    # Arrange
    location1 = {"latitude": 40.7128, "longitude": -74.0060}  # New York
    location2 = {"latitude": 34.0522, "longitude": -74.0060}  # near New York
    # Act
    distance = haversine_distance(location1, location2)
    # Assert
    assert distance > 0
