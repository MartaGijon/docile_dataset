from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    quantity: float = Field(
        ..., description="The number of units or hours for the specific line item"
    )
    description: str = Field(
        ..., description="A textual description of the service or product provided"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the item"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of this line item"
    )


class LineItemList(BaseModel):
    items: List[LineItem] = Field(
        ...,
        description="A list containing the filtered line items matching the query criteria",
    )
