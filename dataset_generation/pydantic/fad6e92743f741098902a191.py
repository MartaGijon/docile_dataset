from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionLine(BaseModel):
    """Represents a single transaction line item filtered by quantity."""

    position: int = Field(
        ..., description="The sequential number of the line item in the document."
    )
    end_date: str = Field(
        ..., description="The end date of the transaction period in MM/DD/YY format."
    )
    total_gross_price: Decimal = Field(
        ..., description="The total gross price for this line item."
    )


class TransactionReport(BaseModel):
    """Container for a list of filtered transaction lines."""

    lines: List[TransactionLine] = Field(
        ..., description="A list of transaction lines matching the query criteria."
    )
