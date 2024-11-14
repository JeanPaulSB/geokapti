import bson
from fastapi import APIRouter, status, Depends
from typing import List
from app.models.locations import Locations
from app.schemas.location import LocationOut, LocationUpdate, Location
from app.core.logger import logger
from app.api.deps import is_valid_location
from app.core.exceptions import LocationNotFound
from bson import ObjectId


router = APIRouter(prefix="/locations", tags=["locations"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=LocationOut)
async def create_location(location: Location):
    location = await Locations(**location.dict()).save()
    logger.info("Saving new location")
    return LocationOut(id=str(location.id))


@router.get("/", response_model=List[Locations])
async def read_locations():
    return await Locations.find_all().to_list()


@router.get("/{location_id}", response_model=Locations)
async def read_location(location_id: str):
    try:
        return await Locations.find_one({"_id": ObjectId(location_id)})
    except bson.errors.InvalidId:
        logger.error(f"Location not found with id {location_id}")
        raise LocationNotFound()


@router.delete("/{location_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_location(location_id: str):
    location = await Locations.find_one(Locations.id == ObjectId(location_id))
    logger.info(f"Deleting location {location_id}")
    await location.delete()


@router.put(
    "/{location_id}", response_model=LocationUpdate, status_code=status.HTTP_200_OK
)
async def update_location(location_id: str, location_data: LocationUpdate):
    try:
        location = await Locations.find_one(Locations.id == ObjectId(location_id))
    except bson.errors.InvalidId:
        logger.error(f"Location not found with id {location_id}")
        raise LocationNotFound()
    await location.update(
        {
            "$set": {
                Locations.name: location_data.name,
                Locations.longitude: location_data.longitude,
                Locations.latitude: location_data.latitude,
            }
        }
    )
    logger.info(f"Updating location {location_id}")
    return location
