from pydantic import BaseModel, validator, field_validator
from typing import List


class Locations(BaseModel):
    ids: List[str]

    @field_validator("ids")
    def check_no_duplicates(cls, v):
        if len(v) != len(set(v)):
            raise ValueError("There are duplicate locations")
        if len(v) < 2:
            raise ValueError("At least 2 locations are required")
        return v
