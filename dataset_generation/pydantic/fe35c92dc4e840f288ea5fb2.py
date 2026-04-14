from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    """Represents a single transaction record filtered by date and price."""

    description: str = Field(
        ..., description="The contract line remarks or description of the transaction."
    )
    price_gross: Decimal = Field(
        ..., description="The gross price of the transaction as a decimal number."
    )


class TransactionList(BaseModel):
    """A container for a list of filtered transaction records."""

    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria."
    )
