from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class BroadcastItem(BaseModel):
    description: str = Field(
        ..., description="The name or title of the news broadcast."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the broadcast as a decimal number."
    )


class BroadcastList(BaseModel):
    items: List[BroadcastItem] = Field(
        ..., description="A list of broadcast items matching the query criteria."
    )
