from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class NewsBroadcastItem(BaseModel):
    description: str = Field(..., description="The name of the news broadcast program")
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the broadcast"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity purchased"
    )


class NewsBroadcastReport(BaseModel):
    items: List[NewsBroadcastItem] = Field(
        ..., description="A list of news broadcast items matching the query criteria"
    )
