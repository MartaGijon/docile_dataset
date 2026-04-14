from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    """Represents a single transaction record filtered by unit price."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format."
    )
    quantity: int = Field(
        ..., description="The number of units sold in this transaction."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction."
    )


class TransactionList(BaseModel):
    """Container for a list of filtered transaction records."""

    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria."
    )
