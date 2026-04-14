from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionLine(BaseModel):
    start_date: str = Field(
        ..., description="The start date of the transaction line item"
    )
    end_date: str = Field(..., description="The end date of the transaction line item")
    unit_price_gross: Decimal = Field(
        ..., description="The gross unit price of the transaction line item"
    )


class TransactionReport(BaseModel):
    lines: List[TransactionLine] = Field(
        ..., description="A list of transaction line items matching the query criteria"
    )
