from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single line item from the transaction query."""

    position: int = Field(
        ..., description="The unique position number of the line item."
    )
    start_date: str = Field(
        ..., description="The start date of the transaction period."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the item."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of this item."
    )


class TransactionList(BaseModel):
    """Container for a list of transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="A list of filtered transaction items."
    )
