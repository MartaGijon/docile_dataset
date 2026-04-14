from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    position: int = Field(
        ..., description="The sequential number of the line item in the document"
    )
    start_date: str = Field(
        ..., description="The starting date of the transaction period"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the item"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of the item"
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria"
    )
