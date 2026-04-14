from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Represents a single transaction line item matching the query criteria."""

    position: int = Field(
        ..., description="The unique position identifier for the transaction line."
    )
    start_date: str = Field(
        ..., description="The start date of the transaction period in MM/DD/YY format."
    )
    end_date: str = Field(
        ..., description="The end date of the transaction period in MM/DD/YY format."
    )
    description: str = Field(
        ..., description="The textual description of the service or item."
    )
    quantity: int = Field(
        ..., description="The number of units for this transaction line."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price for the item as a decimal value."
    )


class TransactionList(BaseModel):
    """A container for a list of transaction items."""

    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query."
    )
