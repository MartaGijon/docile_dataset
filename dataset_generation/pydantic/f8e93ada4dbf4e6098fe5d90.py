from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class SpotItem(BaseModel):
    description: str = Field(
        ..., description="The name of the TV program or news segment"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the spot"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of spots purchased"
    )


class SpotList(BaseModel):
    spots: List[SpotItem] = Field(
        ..., description="A list of all purchased TV spots with non-zero quantities"
    )
