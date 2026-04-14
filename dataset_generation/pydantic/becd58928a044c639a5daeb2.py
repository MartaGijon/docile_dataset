from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    transaction_date: str = Field(
        ..., description="The date the transaction occurred in MM/DD/YY format"
    )
    description: str = Field(
        ..., description="The description or payee name of the transaction"
    )
    amount_net: Decimal = Field(
        ..., description="The net monetary value of the transaction"
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria"
    )
