from typing import Optional
from pydantic import BaseModel
from bson import ObjectId


class Location(BaseModel):
    name: str
    latitude: float
    longitude: float


class LocationOut(BaseModel):
    id: str


class LocationUpdate(BaseModel):
    name: str
    latitude: float
    longitude: float
