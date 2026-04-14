from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class InvoiceLineItem(BaseModel):
    """Represents a single line item on an invoice."""

    description: str = Field(
        ..., description="The textual description of the product or service."
    )
    quantity: int = Field(..., description="The number of units ordered for this item.")
    amount_net: Decimal = Field(
        ..., description="The total net monetary value for this line item."
    )


class InvoiceData(BaseModel):
    """Container for a list of invoice line items."""

    items: List[InvoiceLineItem] = Field(
        ..., description="A list of all parsed invoice line items."
    )
