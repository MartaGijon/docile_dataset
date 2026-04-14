from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class SpotTransaction(BaseModel):
    """Represents a single transaction record for 'Spot' type entries."""

    transaction_date: str = Field(
        ..., description="The date of the transaction in MM/DD/YYYY format."
    )
    description: str = Field(
        ..., description="The description of the transaction, expected to be 'Spot'."
    )
    total_gross_price: Decimal = Field(
        ..., description="The total gross price of the transaction as a decimal number."
    )


class SpotTransactionList(BaseModel):
    """Container for a list of SpotTransaction records."""

    transactions: List[SpotTransaction] = Field(
        ..., description="A list of SpotTransaction objects."
    )
