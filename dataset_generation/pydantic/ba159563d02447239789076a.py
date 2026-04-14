from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class DiscountedPromoItem(BaseModel):
    """Represents a promotional cigarette item with an applied discount."""

    code: str = Field(
        ..., description="The unique product code for the cigarette item."
    )
    description: str = Field(
        ..., description="The textual description of the cigarette product."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the item before any discounts."
    )
    price_gross: Decimal = Field(
        ...,
        description="The final gross price of the item after applying the discount.",
    )


class DiscountedPromoItemsList(BaseModel):
    """A collection of discounted promotional cigarette items."""

    items: List[DiscountedPromoItem] = Field(
        ...,
        description="A list of all discounted promotional items found in the transaction.",
    )
