from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class Transaction(BaseModel):
    """Represents a single sales transaction record."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YYYY format."
    )
    quantity: int = Field(
        ..., description="The number of items sold in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity sold."
    )


class TransactionList(BaseModel):
    """A collection of transaction records."""

    transactions: List[Transaction] = Field(
        ..., description="A list of filtered transaction objects."
    )
