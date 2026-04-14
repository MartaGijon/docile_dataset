from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class CharterIndianapolisTransaction(BaseModel):
    """Represents a single charter transaction to Indianapolis."""

    code: str = Field(..., description="The unique transaction identifier code.")
    description: str = Field(
        ..., description="The description of the transaction, e.g., 'CHR INDIANAPOLIS'."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction."
    )


class CharterIndianapolisTransactionsList(BaseModel):
    """A list of charter transactions to Indianapolis."""

    transactions: List[CharterIndianapolisTransaction] = Field(
        ..., description="List of matching charter transactions."
    )
