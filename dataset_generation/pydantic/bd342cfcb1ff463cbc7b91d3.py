from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item with financial details."""

    quantity: int = Field(
        ..., description="The number of units purchased in this transaction."
    )
    amount_net: Decimal = Field(
        ..., description="The total net monetary value of the transaction line."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity purchased."
    )


class TransactionList(BaseModel):
    """Container for a list of transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="A list of filtered transaction records."
    )
