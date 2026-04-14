from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    transaction_date: str = Field(
        ..., description="The date of the transaction in MM/DD/YYYY format"
    )
    description: str = Field(
        ..., description="The textual description of the transaction"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction as a decimal number"
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria"
    )
