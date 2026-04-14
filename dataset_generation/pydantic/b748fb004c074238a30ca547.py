from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class KXLTransaction(BaseModel):
    description: str = Field(
        ...,
        description="The specific radio station code and date range for the transaction",
    )
    quantity: int = Field(
        ..., description="The number of units sold for this specific line item"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of units sold"
    )


class KXLTransactionList(BaseModel):
    transactions: List[KXLTransaction] = Field(
        ...,
        description="A list containing all KXL transaction records matching the query criteria",
    )
