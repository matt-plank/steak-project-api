from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class NewMeasurement(BaseModel):
    thickness: float
    cookTime: float
    doneness: Literal["RARE"] | Literal["MEDIUM"] | Literal["WELL"]


class Measurement(BaseModel):
    id: str
    thickness: float
    cookTime: float
    doneness: Literal["RARE"] | Literal["MEDIUM"] | Literal["WELL"]


class NewModel(BaseModel):
    coefficients: dict[str, float]
    created: datetime
    doneness: Literal["rare"] | Literal["medium"] | Literal["well"]


class Model(BaseModel):
    id: str
    coefficients: dict[str, float]
    created: datetime
    doneness: Literal["rare"] | Literal["medium"] | Literal["well"]
