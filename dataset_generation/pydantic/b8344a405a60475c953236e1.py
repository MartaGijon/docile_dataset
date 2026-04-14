from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class EveningNewsItem(BaseModel):
    description: str = Field(
        ..., description="The name of the news program or broadcast slot."
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price for a single airing of the program."
    )


class EveningNewsReport(BaseModel):
    items: List[EveningNewsItem] = Field(
        ...,
        description="A list of all evening news broadcast items matching the criteria.",
    )
