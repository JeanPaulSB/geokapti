from app.core.exceptions import BadLocation
from app.schemas.location import Location
from app.core.logger import logger


def is_valid_location(location: Location):
    # latitude must be between -90 deg and 90 deg
    # longitude must be between -180 deg and 180 deg
    if -90 <= location.latitude <= 90 and -180 <= location.longitude <= 180:
        return location
    else:
        logger.error(f"Invalid location: {location}")
        raise BadLocation()
