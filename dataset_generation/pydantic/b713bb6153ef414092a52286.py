from decimal import Decimal
from datetime import date
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item matching the query criteria."""

    position: int = Field(
        ..., description="The unique position identifier for the transaction line."
    )
    start_date: date = Field(
        ..., description="The start date of the transaction period."
    )
    end_date: date = Field(..., description="The end date of the transaction period.")
    quantity: int = Field(
        ..., description="The number of units purchased in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit for this transaction."
    )


class TransactionList(BaseModel):
    """Container for a list of filtered transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items where quantity is greater than 3."
    )
