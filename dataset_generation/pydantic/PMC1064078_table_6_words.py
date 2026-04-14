from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class BirthOrderStats(BaseModel):
    """Represents statistical data for a specific birth order category."""

    birth_order: str = Field(
        ..., description="The birth order category, e.g., '2nd-4th born'."
    )
    race: str = Field(
        ..., description="The race of the participants, e.g., 'African-American'."
    )
    case_count: int = Field(
        ..., description="The number of cases (women with breast cancer) in this group."
    )
    control_count: int = Field(
        ...,
        description="The number of controls (women without breast cancer) in this group.",
    )
    odds_ratio: Decimal = Field(
        ..., description="The minimally adjusted odds ratio for this group."
    )
    ci_lower: Decimal = Field(
        ..., description="The lower bound of the 95% confidence interval."
    )
    ci_upper: Decimal = Field(
        ..., description="The upper bound of the 95% confidence interval."
    )


class BirthOrderStatsList(BaseModel):
    """A container for a list of birth order statistics."""

    stats: List[BirthOrderStats] = Field(
        ..., description="A list of statistical records for different birth orders."
    )
