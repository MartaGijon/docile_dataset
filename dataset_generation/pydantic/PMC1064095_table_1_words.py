from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class BreastCancerRiskData(BaseModel):
    """Represents a single row of breast cancer risk data from the study table."""

    pcb_level: str = Field(
        ...,
        description="The lipid-adjusted total PCB concentration level (e.g., '<0.349' or '>=0.349').",
    )
    genotype: str = Field(
        ..., description="The CYP1A1 genotype status (e.g., 'Non-M2' or 'Any M2')."
    )
    patients_controls: str = Field(
        ...,
        description="The count of patients versus controls in the format 'patients/controls'.",
    )
    odds_ratio: Optional[Decimal] = Field(
        None,
        description="The calculated odds ratio for the specific group; None if it is the referent group.",
    )
    confidence_interval: Optional[str] = Field(
        None,
        description="The 95% confidence interval for the odds ratio as a string range (e.g., '(0.5-1.0)'); None if referent.",
    )
    population_group: str = Field(
        ...,
        description="The specific population subgroup analyzed (e.g., 'All participants', 'Premenopausal', 'Postmenopausal').",
    )


class BreastCancerRiskReport(BaseModel):
    """Container for a list of breast cancer risk data entries."""

    risk_data: List[BreastCancerRiskData] = Field(
        ...,
        description="A list of individual risk data records matching the query criteria.",
    )
