from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class BroadcastTransaction(BaseModel):
    description: str = Field(
        ..., description="The name or title of the broadcast program."
    )
    quantity: int = Field(..., description="The number of times the program was aired.")
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single airing of the program."
    )


class BroadcastTransactionList(BaseModel):
    transactions: List[BroadcastTransaction] = Field(
        ..., description="A list of broadcast transactions matching the query criteria."
    )
