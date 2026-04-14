from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class SpotTransaction(BaseModel):
    """Represents a single spot transaction record."""

    position: str = Field(
        ..., description="The position identifier for the transaction."
    )
    start_date: str = Field(
        ..., description="The start date of the transaction period."
    )
    end_date: str = Field(..., description="The end date of the transaction period.")
    quantity: int = Field(..., description="The quantity of items in the transaction.")
    description: str = Field(
        ..., description="The description or type of the transaction."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the item."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction."
    )


class SpotTransactionList(BaseModel):
    """A list of spot transaction records."""

    transactions: List[SpotTransaction] = Field(
        ..., description="A list containing multiple spot transaction records."
    )
