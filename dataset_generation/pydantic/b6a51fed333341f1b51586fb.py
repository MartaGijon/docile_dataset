from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    position: int = Field(
        ..., description="The sequential number of the line item in the document"
    )
    quantity: int = Field(
        ..., description="The number of units purchased for this specific line item"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit for this line item"
    )


class LineItemList(BaseModel):
    items: List[LineItem] = Field(
        ..., description="A list of filtered line items matching the query criteria"
    )
