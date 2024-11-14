import httpx
from fastapi import APIRouter
from typing import List
from app.schemas.locations import Locations
from app.external_services.location import fetch_locations

router = APIRouter(prefix="/distances", tags=["distances"])


@router.post("/")
async def compute_distance(locations: Locations):
    result = await fetch_locations(locations.ids)
    print(result)

