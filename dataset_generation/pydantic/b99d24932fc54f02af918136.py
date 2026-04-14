from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    """Represents a single transaction entry filtered by price."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format."
    )
    description: str = Field(
        ..., description="The textual description of the transaction item."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number."
    )


class TransactionList(BaseModel):
    """Container for a list of filtered transaction records."""

    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria."
    )
