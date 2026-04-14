from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class AdSlot(BaseModel):
    description: str = Field(
        ...,
        description="The name or description of the advertising slot, e.g., 'M-F AM Drive'.",
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the advertising slot."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit for the advertising slot."
    )


class AdSlotList(BaseModel):
    slots: List[AdSlot] = Field(
        ..., description="A list of advertising slots matching the query criteria."
    )
