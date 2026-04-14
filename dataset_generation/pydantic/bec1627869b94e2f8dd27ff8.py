from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class SpotTransaction(BaseModel):
    """Represents a single spot transaction record."""

    transaction_date: str = Field(
        ..., description="The date of the transaction in MM/DD/YYYY format."
    )
    description: str = Field(
        ..., description="The description of the transaction, e.g., 'Spot'."
    )
    code: str = Field(
        ..., description="The unique code identifier for the transaction."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction as a decimal number."
    )


class SpotTransactionList(BaseModel):
    """A container for a list of spot transactions."""

    transactions: List[SpotTransaction] = Field(
        ..., description="A list of SpotTransaction objects."
    )
