from decimal import Decimal
from datetime import date
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item filtered by quantity."""

    transaction_date: date = Field(..., description="The date of the transaction.")
    quantity: int = Field(
        ..., description="The number of units purchased in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity purchased."
    )


class TransactionList(BaseModel):
    """A collection of filtered transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="List of transactions where quantity is greater than 1."
    )
