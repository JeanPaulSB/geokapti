from pydantic import BaseModel, Field


class Location(BaseModel):
    name: str
    latitude: float = Field(
        ..., description="Must be between -90 deg and 90 deg", ge=-90, le=90
    )
    longitude: float = Field(
        ..., description="Must be between -180 deg and 180 deg", ge=-180, le=180
    )
