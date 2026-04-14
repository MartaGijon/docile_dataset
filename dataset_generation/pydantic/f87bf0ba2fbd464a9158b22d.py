from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class NewsLineItem(BaseModel):
    description: str = Field(
        ..., description="The text description of the news line item"
    )
    quantity: int = Field(..., description="The number of units purchased")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity purchased"
    )


class NewsLineItemsList(BaseModel):
    items: List[NewsLineItem] = Field(
        ..., description="A list of news line items matching the query criteria"
    )
