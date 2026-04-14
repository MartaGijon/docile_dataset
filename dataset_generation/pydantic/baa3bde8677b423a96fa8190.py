from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    time_period: str = Field(
        ...,
        description="The specific time slot and day range for the transaction, e.g., 'Morning, M-F, 6a-10am, 30'",
    )
    total_gross_price: Decimal = Field(
        ..., description="The total gross price for the specific transaction line item"
    )


class TransactionList(BaseModel):
    items: List[TransactionItem] = Field(
        ..., description="A list of transaction items matching the query criteria"
    )
