from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class WeekendShift(BaseModel):
    description: str = Field(
        ..., description="The time slot and day description for the shift"
    )
    quantity: int = Field(..., description="The number of units booked for this shift")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit for this shift"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of this shift"
    )


class WeekendShiftsReport(BaseModel):
    shifts: List[WeekendShift] = Field(
        ...,
        description="A list of all weekend shift records matching the query criteria",
    )
