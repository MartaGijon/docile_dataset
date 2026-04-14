from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class WeekdaySpot(BaseModel):
    description: str = Field(
        ..., description="The name and time slot of the advertising program"
    )
    quantity: int = Field(..., description="The number of times the ad aired")
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of ads"
    )


class WeekdaySpotsReport(BaseModel):
    spots: List[WeekdaySpot] = Field(
        ..., description="A list of all qualifying weekday advertising spots"
    )
