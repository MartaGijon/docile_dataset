from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class NewsTransaction(BaseModel):
    description: str = Field(..., description="The name or title of the news program")
    code: str = Field(
        ..., description="The unique alphanumeric identifier for the transaction"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction as a decimal number"
    )


class NewsTransactionList(BaseModel):
    transactions: List[NewsTransaction] = Field(
        ..., description="A list containing all retrieved news transaction records"
    )
