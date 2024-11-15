from pydantic import BaseModel, validator, field_validator
from typing import List


class TotalDistanceResult(BaseModel):
    total_distance: float
