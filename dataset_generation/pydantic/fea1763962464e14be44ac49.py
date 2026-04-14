from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    transaction_date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format"
    )
    quantity_sold: int = Field(
        ..., description="The number of units sold in this transaction"
    )
    total_gross_price: Decimal = Field(
        ...,
        description="The total gross price for the transaction calculated as quantity times unit price",
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria"
    )
