from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class ArbitrationServiceItem(BaseModel):
    description: str = Field(
        ..., description="Detailed description of the arbitration service performed"
    )
    quantity: Decimal = Field(
        ..., description="Number of hours or units of service provided"
    )
    unit_price_gross: Decimal = Field(
        ..., description="Gross price per unit of service"
    )
    price_gross: Decimal = Field(
        ..., description="Total gross price for the service line item"
    )


class ArbitrationServicesList(BaseModel):
    items: List[ArbitrationServiceItem] = Field(
        ...,
        description="List of specific arbitration service transactions matching the query criteria",
    )
