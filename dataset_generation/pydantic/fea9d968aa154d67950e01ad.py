from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction record filtered by quantity."""

    position: int = Field(
        ..., description="The unique position identifier for the transaction."
    )
    date: str = Field(..., description="The date the transaction occurred.")
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the item as a decimal."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction line as a decimal."
    )


class TransactionList(BaseModel):
    """A collection of filtered transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria."
    )
