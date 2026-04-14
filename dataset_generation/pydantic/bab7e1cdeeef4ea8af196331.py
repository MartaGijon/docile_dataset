from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    description: str = Field(
        ..., description="The name or title of the media item or service."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the item."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of items."
    )


class LineItemList(BaseModel):
    items: List[LineItem] = Field(
        ..., description="A list of line items matching the query criteria."
    )
