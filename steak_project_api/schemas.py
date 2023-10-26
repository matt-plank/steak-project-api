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
