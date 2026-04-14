from decimal import Decimal
from datetime import date
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    transaction_date: date = Field(
        ..., description="The date the transaction occurred in YYYY-MM-DD format."
    )
    quantity: int = Field(
        ..., description="The number of units sold in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ...,
        description="The gross price per single unit, stored as a decimal to ensure precision.",
    )
    price_gross: Decimal = Field(
        ...,
        description="The total gross price for the quantity sold, stored as a decimal to ensure precision.",
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria."
    )
