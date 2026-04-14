from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class WeekendSpot(BaseModel):
    description: str = Field(
        ..., description="The name or time slot of the advertising spot"
    )
    quantity: int = Field(..., description="The number of times the spot aired")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single airing of the spot"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for all airings of the spot"
    )


class WeekendSpotsReport(BaseModel):
    spots: List[WeekendSpot] = Field(
        ..., description="A list of all weekend advertising spots matching the criteria"
    )
