import httpx
from typing import List
# fetches location's information on locations microservice
async def fetch_locations(locations_ids: List[str]):
    locations = []
    for location_id in locations_ids:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"http://locations_service:8081/locations/{location_id}")
                if response.status_code == 200:
                    locations.append(response.json())
                else:
                    return {"error": f"Failed to fetch location {location_id}, status code {response.status_code}"}
        except httpx.RequestError as exc:
            return {"error": f"Request error for location {location_id}: {exc}"}
    return locations