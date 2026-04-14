from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item matching the query criteria."""

    description: str = Field(
        ...,
        description="The name or identifier of the service or product, e.g., 'WMPX-AM'.",
    )
    quantity: int = Field(
        ..., description="The number of units purchased in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ...,
        description="The gross price per single unit, stored as a Decimal for precision.",
    )
    price_gross: Decimal = Field(
        ...,
        description="The total gross price for the quantity purchased, stored as a Decimal for precision.",
    )


class TransactionList(BaseModel):
    """Container for a list of filtered transaction items."""

    items: List[TransactionItem] = Field(
        ...,
        description="A list of transaction items that match the specific unit price filter.",
    )
