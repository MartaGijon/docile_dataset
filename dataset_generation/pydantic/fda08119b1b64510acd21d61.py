from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    code: str = Field(..., description="The unique transaction identifier code")
    description: str = Field(..., description="The text description of the transaction")
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number"
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria"
    )
