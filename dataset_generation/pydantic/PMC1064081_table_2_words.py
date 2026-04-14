from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class HazardRatioEntry(BaseModel):
    """Represents a single hazard ratio analysis entry for a specific nodal variable."""

    model_id: int = Field(
        ...,
        description="The unique identifier for the statistical model (e.g., 2, 6, 9).",
    )
    nodal_variable: str = Field(
        ..., description="The specific nodal variable being analyzed (e.g., 'np', 'L')."
    )
    hazard_ratio: Decimal = Field(
        ..., description="The calculated hazard ratio indicating the risk level."
    )
    confidence_interval_lower: Decimal = Field(
        ..., description="The lower bound of the 95% confidence interval."
    )
    confidence_interval_upper: Decimal = Field(
        ..., description="The upper bound of the 95% confidence interval."
    )


class HazardRatioReport(BaseModel):
    """Container for a list of hazard ratio entries."""

    entries: List[HazardRatioEntry] = Field(
        ..., description="A list of hazard ratio analysis results."
    )
