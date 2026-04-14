from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    code: str = Field(..., description="The unique transaction code identifier")
    description: str = Field(
        ..., description="The textual description of the service or item"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number"
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria"
    )
