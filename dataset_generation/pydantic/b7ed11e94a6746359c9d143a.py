from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    transaction_date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction as a decimal number"
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria"
    )
