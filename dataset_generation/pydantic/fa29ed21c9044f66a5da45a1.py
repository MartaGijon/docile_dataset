from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field
from datetime import date


class OctoberTransaction(BaseModel):
    transaction_date: date = Field(
        ..., description="The date the transaction occurred in October 2020"
    )
    quantity: int = Field(
        ..., description="The number of items purchased, specifically 3"
    )
    total_gross_price: Decimal = Field(
        ..., description="The total gross price for the transaction"
    )


class OctoberTransactionList(BaseModel):
    transactions: List[OctoberTransaction] = Field(
        ..., description="A list of all matching October 2020 transactions"
    )
