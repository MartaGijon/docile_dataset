from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class RegressionFeature(BaseModel):
    feature_name: str = Field(
        ..., description="The name of the clinical feature, e.g., 'Age' or 'Grade'."
    )
    feature_type: str = Field(
        ..., description="The type of the feature, e.g., 'continuous'."
    )
    odds_ratio: Decimal = Field(
        ..., description="The calculated odds ratio for the feature in the BRCA1 group."
    )
    confidence_interval: str = Field(
        ..., description="The 95% confidence interval range for the odds ratio."
    )
    p_value: str = Field(
        ..., description="The p-value indicating statistical significance."
    )


class RegressionResultList(BaseModel):
    results: List[RegressionFeature] = Field(
        ...,
        description="A list of regression feature results for the specified analysis step.",
    )
