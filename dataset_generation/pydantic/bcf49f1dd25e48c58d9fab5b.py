from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionLine(BaseModel):
    """Represents a single transaction line item filtered by quantity."""

    position: int = Field(
        ..., description="The sequential position number of the line item."
    )
    start_date: str = Field(
        ..., description="The start date of the transaction period."
    )
    end_date: str = Field(..., description="The end date of the transaction period.")
    quantity: int = Field(..., description="The number of units purchased.")
    price_gross: Decimal = Field(
        ..., description="The total gross price for the line item."
    )


class TransactionReport(BaseModel):
    """Container for a list of filtered transaction lines."""

    lines: List[TransactionLine] = Field(
        ..., description="A list of transaction lines matching the query criteria."
    )
