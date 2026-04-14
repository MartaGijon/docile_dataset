from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    """Represents a single financial transaction record."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format."
    )
    position: int = Field(
        ..., description="The position number associated with the transaction."
    )
    description: str = Field(
        ..., description="The description of the transaction item."
    )
    unit_price_net: Decimal = Field(
        ..., description="The net unit price of the transaction as a decimal."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction line as a decimal."
    )


class TransactionList(BaseModel):
    """Container for a list of transaction records."""

    transactions: List[TransactionRecord] = Field(
        ..., description="A list of individual transaction records."
    )
