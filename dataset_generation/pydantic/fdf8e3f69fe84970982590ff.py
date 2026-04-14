from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    description: str = Field(
        ..., description="The location or station name for the transaction"
    )
    code: str = Field(
        ..., description="The transaction type code, e.g., Normal Line / SPOT"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction line item"
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ...,
        description="A list of filtered transaction items matching the query criteria",
    )
