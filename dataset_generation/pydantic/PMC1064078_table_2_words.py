from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class BirthweightStats(BaseModel):
    """Represents statistical data for a specific birthweight tertile."""

    tertile_group: str = Field(
        ...,
        description="The birthweight tertile category (e.g., Lower, Central, Upper).",
    )
    cases_count: int = Field(
        ..., description="The number of breast cancer cases in this group."
    )
    controls_count: int = Field(
        ..., description="The number of control subjects in this group."
    )
    odds_ratio_minimally_adjusted: Optional[Decimal] = Field(
        None, description="The minimally adjusted odds ratio for breast cancer risk."
    )
    confidence_interval_lower: Optional[Decimal] = Field(
        None, description="The lower bound of the 95% confidence interval."
    )
    confidence_interval_upper: Optional[Decimal] = Field(
        None, description="The upper bound of the 95% confidence interval."
    )


class BirthweightStatsList(BaseModel):
    """Container for a list of birthweight statistics."""

    stats: List[BirthweightStats] = Field(
        ...,
        description="A list of statistical records for different birthweight groups.",
    )
