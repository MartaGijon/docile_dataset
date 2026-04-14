from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    description: str = Field(
        ..., description="The textual description of the product or service"
    )
    quantity: int = Field(..., description="The number of units ordered")
    price_gross: Decimal = Field(
        ..., description="The total gross price for the line item"
    )


class LineItemList(BaseModel):
    items: List[LineItem] = Field(
        ..., description="A list of filtered line items matching the query criteria"
    )
