from pydantic import BaseModel, validator, field_validator
from typing import List


class Task(BaseModel):
    status: str
    id: str
