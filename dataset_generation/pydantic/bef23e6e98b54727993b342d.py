from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the item before tax."
    )
    unit_price_net: Decimal = Field(
        ..., description="The net unit price of the item after tax."
    )
    quantity: int = Field(..., description="The number of units purchased.")


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria."
    )
