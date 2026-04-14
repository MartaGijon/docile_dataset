from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field
from datetime import date


class TransactionRecord(BaseModel):
    transaction_date: date = Field(
        ..., description="The specific date when the transaction occurred."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the item involved in the transaction."
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list containing all filtered transaction records."
    )
