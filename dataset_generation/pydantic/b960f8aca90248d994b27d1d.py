from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class SpotTransaction(BaseModel):
    """Represents a single Spot transaction record."""

    date: str = Field(
        ..., description="The date of the transaction in MM/DD/YYYY format."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit for the transaction."
    )


class SpotTransactionList(BaseModel):
    """Container for a list of Spot transactions."""

    transactions: List[SpotTransaction] = Field(
        ..., description="A list of SpotTransaction objects."
    )
