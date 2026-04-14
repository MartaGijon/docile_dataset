from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class GenotypeData(BaseModel):
    genotype: str = Field(
        ..., description="The specific genetic variant combination, e.g., 'Ala/Ala'"
    )
    cases_count: int = Field(
        ..., description="The number of case subjects with this genotype"
    )
    cases_percentage: float = Field(
        ..., description="The percentage of cases represented by this genotype"
    )
    odds_ratio: Decimal = Field(
        ...,
        description="The calculated odds ratio for this genotype compared to the reference",
    )
    confidence_interval: str = Field(
        ..., description="The 95% confidence interval for the odds ratio"
    )


class GenotypeDataList(BaseModel):
    data: List[GenotypeData] = Field(
        ..., description="A list of genotype records for the specified subgroup"
    )
