from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class DrOzTransaction(BaseModel):
    """Represents a single transaction for Dr. Oz with quantity greater than 1."""

    description: str = Field(..., description="The name of the program or service.")
    quantity: int = Field(..., description="The number of units purchased.")
    price_gross: Decimal = Field(
        ..., description="The total gross price for the transaction."
    )
    unit_price_gross: Decimal = Field(..., description="The gross price per unit.")


class DrOzTransactionList(BaseModel):
    """A list of Dr. Oz transactions matching the query criteria."""

    transactions: List[DrOzTransaction] = Field(
        ..., description="List of filtered Dr. Oz transactions."
    )
