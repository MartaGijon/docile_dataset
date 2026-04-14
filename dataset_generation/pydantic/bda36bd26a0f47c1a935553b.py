from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item filtered by unit price."""

    code: str = Field(
        ..., description="The program code or identifier for the transaction."
    )
    quantity: int = Field(
        ..., description="The number of units sold in this transaction."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity sold."
    )


class TransactionList(BaseModel):
    """A collection of filtered transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="List of transaction items matching the query criteria."
    )
