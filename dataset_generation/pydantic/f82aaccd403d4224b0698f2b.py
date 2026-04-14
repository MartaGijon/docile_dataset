from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class NewsProgramItem(BaseModel):
    description: str = Field(..., description="The name of the news program")
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the program"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity ordered"
    )


class NewsProgramList(BaseModel):
    items: List[NewsProgramItem] = Field(
        ..., description="A list of news program items matching the query criteria"
    )
