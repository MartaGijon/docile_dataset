from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class AdSpot(BaseModel):
    description: str = Field(
        ..., description="The name or title of the advertising program or slot"
    )
    unit_price_gross: Decimal = Field(
        ..., description="The gross price per single unit of the advertising spot"
    )
    price_gross: Decimal = Field(
        ..., description="The total gross price for the quantity of spots purchased"
    )


class AdSpotReport(BaseModel):
    spots: List[AdSpot] = Field(
        ...,
        description="A list of high-value advertising spots matching the query criteria",
    )
