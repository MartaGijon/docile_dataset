from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class MaternalAgeOddsRatio(BaseModel):
    """Represents a single record of odds ratio data for a specific maternal age group."""

    age_group: str = Field(
        ..., description="The maternal age range in years, e.g., '23-27'."
    )
    case_count: int = Field(
        ..., description="The number of cases observed in this age group."
    )
    control_count: int = Field(
        ..., description="The number of controls observed in this age group."
    )
    minimally_adjusted_or: Decimal = Field(
        ..., description="The minimally adjusted odds ratio for breast cancer risk."
    )
    confidence_interval_lower: Decimal = Field(
        ..., description="The lower bound of the 95% confidence interval."
    )
    confidence_interval_upper: Decimal = Field(
        ..., description="The upper bound of the 95% confidence interval."
    )


class MaternalAgeOddsRatioList(BaseModel):
    """Container for a list of maternal age odds ratio records."""

    records: List[MaternalAgeOddsRatio] = Field(
        ..., description="A list of odds ratio records filtered by specific criteria."
    )
