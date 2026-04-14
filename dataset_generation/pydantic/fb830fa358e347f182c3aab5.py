from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    """Represents a single financial transaction record."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format."
    )
    description: str = Field(
        ...,
        description="A textual description of the transaction, including payee and reference codes.",
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number."
    )


class TransactionList(BaseModel):
    """A container for a list of transaction records."""

    transactions: List[TransactionRecord] = Field(
        ...,
        description="A list of individual transaction records matching the query criteria.",
    )
