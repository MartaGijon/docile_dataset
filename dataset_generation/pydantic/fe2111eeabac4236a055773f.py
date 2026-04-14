from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the item."
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the specific quantity of the item."
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria."
    )
