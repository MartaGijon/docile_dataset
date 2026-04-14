from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class MaternalAgeOddsRatio(BaseModel):
    """Represents a single row of odds ratio data for a specific maternal age group."""

    age_group: str = Field(..., description="The maternal age range, e.g., '23-27'.")
    race: str = Field(
        ..., description="The race of the women, e.g., 'African-American'."
    )
    case_count: int = Field(..., description="The number of cases in this group.")
    control_count: int = Field(..., description="The number of controls in this group.")
    odds_ratio: Decimal = Field(
        ..., description="The minimally adjusted odds ratio for breast cancer risk."
    )
    ci_lower: Decimal = Field(
        ..., description="The lower bound of the 95% confidence interval."
    )
    ci_upper: Decimal = Field(
        ..., description="The upper bound of the 95% confidence interval."
    )


class MaternalAgeOddsRatioList(BaseModel):
    """Container for a list of maternal age odds ratio records."""

    records: List[MaternalAgeOddsRatio] = Field(
        ..., description="A list of odds ratio records for the specified query."
    )
