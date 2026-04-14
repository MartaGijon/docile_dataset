from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class TransactionRecord(BaseModel):
    """Represents a single transaction record with date, quantity, and price details."""

    transaction_date: int = Field(
        ..., description="The day of the month the transaction occurred (1-31)."
    )
    quantity: int = Field(
        ..., description="The number of items purchased in this transaction."
    )
    unit_price_gross: Decimal = Field(
        ...,
        description="The gross price per single unit, calculated from total price and quantity.",
    )
    price_gross: Decimal = Field(
        ...,
        description="The total gross price for the entire quantity in this transaction.",
    )


class TransactionReport(BaseModel):
    """A report containing a list of filtered transaction records."""

    transactions: List[TransactionRecord] = Field(
        ..., description="A list of transaction records matching the query criteria."
    )
