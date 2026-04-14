from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    start_date: str = Field(
        ...,
        description="The starting date of the transaction period in MM/DD/YY format.",
    )
    end_date: str = Field(
        ..., description="The ending date of the transaction period in MM/DD/YY format."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction as a decimal number."
    )


class TransactionList(BaseModel):
    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria."
    )
