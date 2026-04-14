from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    transaction_date: str = Field(
        ..., description="The date of the transaction in MM/DD/YY format"
    )
    description: str = Field(
        ...,
        description="The description or merchant name associated with the transaction",
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price of a single unit in the transaction"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction line item"
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria"
    )
