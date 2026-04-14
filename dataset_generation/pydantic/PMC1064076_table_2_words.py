from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class GenotypeRisk(BaseModel):
    """Represents the risk association for a specific MnSOD genotype in a defined subgroup."""

    menopausal_status: str = Field(
        ..., description="Menopausal status of the group, e.g., 'Postmenopausal'"
    )
    bmi_category: str = Field(
        ..., description="BMI category relative to the median, e.g., '> Median'"
    )
    genotype: str = Field(
        ..., description="The specific MnSOD genotype, e.g., 'Val/Ala' or 'Ala/Ala'"
    )
    cases_controls: str = Field(
        ..., description="Ratio of cases to controls for this genotype group"
    )
    odds_ratio: Decimal = Field(
        ..., description="The adjusted odds ratio for breast cancer risk"
    )
    confidence_interval: str = Field(
        ..., description="The 95% confidence interval for the odds ratio"
    )


class GenotypeRiskList(BaseModel):
    """Container for a list of genotype risk associations."""

    risks: List[GenotypeRisk] = Field(
        ..., description="List of specific genotype risk records"
    )
