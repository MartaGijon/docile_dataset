from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    description: str = Field(
        ..., description="The name or identifier of the service or product."
    )
    start_date: str = Field(
        ..., description="The starting date of the transaction period."
    )
    end_date: str = Field(..., description="The ending date of the transaction period.")
    quantity: int = Field(..., description="The number of units purchased.")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity purchased."
    )


class LineItemsList(BaseModel):
    items: List[LineItem] = Field(
        ..., description="A list of line items matching the query criteria."
    )
