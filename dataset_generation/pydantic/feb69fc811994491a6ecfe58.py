from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class AdPosition(BaseModel):
    description: str = Field(
        ..., description="The name of the TV show or program being advertised"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the advertisement"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of advertisements"
    )


class AdPositionList(BaseModel):
    items: List[AdPosition] = Field(
        ..., description="A list of advertising positions matching the query criteria"
    )
