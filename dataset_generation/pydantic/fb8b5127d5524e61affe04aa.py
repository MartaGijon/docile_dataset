from decimal import Decimal
from datetime import date
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    transaction_date: date = Field(..., description="The date the transaction occurred")
    gross_unit_price: Decimal = Field(
        ..., description="The gross unit price of the transaction"
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria"
    )
