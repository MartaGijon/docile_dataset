from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    description: str = Field(
        ..., description="The name or title of the transaction item"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price of the transaction item"
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria"
    )
