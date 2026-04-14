from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class SpotTransaction(BaseModel):
    """Represents a single spot line transaction with a specific gross price."""

    code: str = Field(
        ..., description="The transaction code, e.g., 'Normal Line / SPOT'"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction as a decimal number"
    )


class SpotTransactionList(BaseModel):
    """A collection of spot line transactions matching the query criteria."""

    transactions: List[SpotTransaction] = Field(
        ..., description="List of matching spot transactions"
    )
