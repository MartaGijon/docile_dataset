from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class BreastCancerRisk(BaseModel):
    """Represents the breast cancer risk data for a specific birthweight tertile."""

    race: str = Field(
        ..., description="The race of the women, e.g., 'African-American' or 'White'."
    )
    dataset_type: str = Field(
        ...,
        description="The dataset used, e.g., 'Full birthweight dataset' or 'Restricted dataset'.",
    )
    tertile: str = Field(
        ...,
        description="The birthweight tertile category, e.g., 'Lower tertile', 'Central tertile', 'Upper tertile'.",
    )
    cases: int = Field(
        ..., description="The number of breast cancer cases in this group."
    )
    controls: int = Field(..., description="The number of controls in this group.")
    odds_ratio: Decimal = Field(
        ..., description="The fully adjusted odds ratio for breast cancer risk."
    )
    confidence_interval_lower: Decimal = Field(
        ..., description="The lower bound of the 95% confidence interval."
    )
    confidence_interval_upper: Decimal = Field(
        ..., description="The upper bound of the 95% confidence interval."
    )


class BreastCancerRiskList(BaseModel):
    """A list of breast cancer risk records."""

    records: List[BreastCancerRisk] = Field(
        ..., description="A list of BreastCancerRisk objects."
    )
