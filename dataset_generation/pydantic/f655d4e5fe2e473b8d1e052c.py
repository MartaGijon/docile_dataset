from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class CigaretteTransaction(BaseModel):
    """Represents a single cigarette transaction line item."""

    code: str = Field(..., description="The unique product code identifier.")
    description: str = Field(
        ..., description="The textual description of the cigarette product."
    )
    amount_net: Decimal = Field(
        ..., description="The total net monetary value for this line item."
    )
    unit_price_net: Decimal = Field(
        ..., description="The net price per single unit of the product."
    )


class CigaretteTransactionList(BaseModel):
    """A collection of cigarette transaction line items."""

    transactions: List[CigaretteTransaction] = Field(
        ..., description="A list of filtered cigarette transaction records."
    )
