from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    position: int = Field(
        ...,
        description="The unique sequential identifier of the transaction line item.",
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per unit for the specific transaction line."
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ...,
        description="A list containing all transaction records matching the specified date range criteria.",
    )
