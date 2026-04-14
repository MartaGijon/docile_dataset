from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format."
    )
    description: str = Field(
        ..., description="The description of the service or item, e.g., 'M-F 6a-7p'."
    )
    quantity: int = Field(
        ..., description="The number of units purchased in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit as a decimal number."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for this line item as a decimal number."
    )


class TransactionList(BaseModel):
    """A collection of transaction items."""

    transactions: List[TransactionItem] = Field(
        ..., description="A list of all matching transaction items."
    )
