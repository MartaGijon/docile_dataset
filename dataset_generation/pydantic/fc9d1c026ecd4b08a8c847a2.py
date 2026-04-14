from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionLineItem(BaseModel):
    quantity: int = Field(
        ..., description="The number of units purchased in this specific line item."
    )
    price_gross: Decimal = Field(
        ...,
        description="The total gross price for this line item calculated as quantity multiplied by unit price.",
    )


class TransactionList(BaseModel):
    items: List[TransactionLineItem] = Field(
        ...,
        description="A list of filtered transaction line items matching the query criteria.",
    )
