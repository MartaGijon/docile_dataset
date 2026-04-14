from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class ShowItem(BaseModel):
    description: str = Field(..., description="The name of the TV show or program")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the show"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of the show"
    )


class ShowItemsList(BaseModel):
    items: List[ShowItem] = Field(
        ..., description="A list of TV show items matching the query criteria"
    )
