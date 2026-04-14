from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class ClinicalFactorData(BaseModel):
    """Represents a specific clinical or pathological factor category and its associated patient counts."""

    factor_category: str = Field(
        ...,
        description="The specific clinical factor category, e.g., 'Age', 'Tumour size'.",
    )
    sub_category: str = Field(
        ...,
        description="The specific sub-category within the factor, e.g., '≥50', 'T2 (>2.0 cm to ≤5.0 cm)'.",
    )
    low_expression_count: int = Field(
        ...,
        description="The number of patients with low LPA2 expression in this sub-category.",
    )
    low_expression_percentage: Decimal = Field(
        ...,
        description="The percentage of patients with low LPA2 expression in this sub-category.",
    )
    high_expression_count: int = Field(
        ...,
        description="The number of patients with high LPA2 expression in this sub-category.",
    )
    high_expression_percentage: Decimal = Field(
        ...,
        description="The percentage of patients with high LPA2 expression in this sub-category.",
    )


class ClinicalFactorDataList(BaseModel):
    """A container for a list of clinical factor data entries."""

    data: List[ClinicalFactorData] = Field(
        ..., description="A list of clinical factor data entries."
    )
