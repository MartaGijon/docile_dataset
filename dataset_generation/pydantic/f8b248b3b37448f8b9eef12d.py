from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class AdSpot(BaseModel):
    description: str = Field(
        ...,
        description="The text description of the advertising spot, e.g., 'M-F 830-9a News'.",
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the specific line item."
    )
    quantity: int = Field(
        ..., description="The number of units purchased for this spot."
    )


class AdSpotList(BaseModel):
    spots: List[AdSpot] = Field(
        ..., description="A list of advertising spots matching the query criteria."
    )
