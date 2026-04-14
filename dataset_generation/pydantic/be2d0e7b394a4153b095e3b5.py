from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class CigaretteTransaction(BaseModel):
    """Represents a single cigarette transaction line item."""

    description: str = Field(
        ..., description="The specific name and variant of the cigarette product."
    )
    unit_price_gross: Decimal = Field(
        ...,
        description="The gross price per single unit (e.g., per carton) as a decimal number.",
    )
    price_gross: Decimal = Field(
        ...,
        description="The total gross price for the entire quantity purchased as a decimal number.",
    )


class CigaretteTransactionList(BaseModel):
    """A collection of cigarette transaction line items."""

    transactions: List[CigaretteTransaction] = Field(
        ..., description="A list of individual cigarette transaction records."
    )
