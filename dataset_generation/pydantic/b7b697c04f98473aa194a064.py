from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class LineItem(BaseModel):
    """Represents a single line item from the transaction."""

    position: int = Field(
        ..., description="The sequential position number of the line item."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit for this line item."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for this line item."
    )


class LineItemList(BaseModel):
    """Container for a list of filtered line items."""

    items: List[LineItem] = Field(
        ..., description="A list of line items matching the query criteria."
    )
