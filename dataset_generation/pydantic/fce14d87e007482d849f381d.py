from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionLineItem(BaseModel):
    """Represents a single line item from a transaction record."""

    position: int = Field(
        ..., description="The sequential number of the line item in the document."
    )
    start_date: str = Field(
        ..., description="The start date of the transaction period."
    )
    end_date: str = Field(..., description="The end date of the transaction period.")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the item."
    )
    quantity: int = Field(
        ..., description="The number of units purchased in this line item."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of this line item."
    )


class TransactionReport(BaseModel):
    """A report containing a list of filtered transaction line items."""

    items: List[TransactionLineItem] = Field(
        ..., description="A list of transaction line items matching the query criteria."
    )
