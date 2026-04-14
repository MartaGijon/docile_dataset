from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class WeekendShiftItem(BaseModel):
    description: str = Field(
        ..., description="The text description of the shift, e.g., 'Sa-Su 10a-3p'"
    )
    quantity: int = Field(
        ..., description="The number of shifts or hours for this specific line item"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit for this shift"
    )


class WeekendShiftReport(BaseModel):
    items: List[WeekendShiftItem] = Field(
        ...,
        description="A list of all weekend shift entries matching the query criteria",
    )
