from fastapi import APIRouter,status
from typing import List
from app.models.locations import Locations
from app.schemas.location import LocationOut
from app.core.logger import logger
router = APIRouter(prefix="/locations", tags=["locations"])

# TODO: define endpoints, validate lat and lon before saving
@router.post("/",status_code = status.HTTP_201_CREATED,response_model=LocationOut)
async def create_location(location: Locations):
    location = await location.save()
    logger.info("Saving new location")
    return LocationOut(id = str(location.id))

@router.get("/",response_model=List[Locations])
async def read_locations():
    return await Locations.find_all().to_list()
