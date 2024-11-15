import httpx
from typing import List
from app.core.logger import logger
from app.core.exceptions import LocationNotFound


# fetches location's information on locations microservice
async def fetch_locations(locations_ids: List[str]):
    locations = []
    for location_id in locations_ids:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"http://locations_service:8081/locations/{location_id}"
                )
                if response.status_code == 200:
                    logger.info(f"Retrieved location successfully {location_id}")
                    locations.append(response.json())
                else:
                    logger.error(f"Failed to retrieve location {location_id}")
                    raise LocationNotFound()

        except httpx.RequestError as exc:
            logger.error(exc)
            return {"error": f"Request error for location {location_id}: {exc}"}
    return locations
