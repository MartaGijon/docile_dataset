from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class GenotypeAssociation(BaseModel):
    """Represents the statistical association data for a specific genotype."""

    genotype: str = Field(
        ...,
        description="The specific manganese superoxide dismutase genotype (e.g., Val/Val, Val/Ala, Ala/Ala).",
    )
    cases_controls: str = Field(
        ...,
        description="The count of cases versus controls for this genotype group (format: 'cases/controls').",
    )
    odds_ratio: Decimal = Field(
        ...,
        description="The adjusted odds ratio for breast cancer risk associated with this genotype.",
    )
    confidence_interval_lower: Optional[Decimal] = Field(
        None,
        description="The lower bound of the 95% confidence interval for the odds ratio.",
    )
    confidence_interval_upper: Optional[Decimal] = Field(
        None,
        description="The upper bound of the 95% confidence interval for the odds ratio.",
    )
    is_reference: bool = Field(
        False,
        description="Indicates if this genotype is the reference group (odds ratio = 1.0).",
    )


class StratifiedAnalysisResult(BaseModel):
    """Container for the analysis results of a specific stratification group."""

    stratification_variable: str = Field(
        ...,
        description="The variable used for stratification (e.g., 'Total vegetables').",
    )
    stratification_level: str = Field(
        ..., description="The specific level of the variable (e.g., '> Median')."
    )
    population_group: str = Field(
        ...,
        description="The demographic group being analyzed (e.g., 'Postmenopausal women').",
    )
    genotypes: List[GenotypeAssociation] = Field(
        ...,
        description="List of association data for each genotype within this stratum.",
    )
