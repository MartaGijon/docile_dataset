from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class BreastCancerRiskData(BaseModel):
    """Represents a single record of breast cancer risk odds ratios based on PCB levels and genotype."""

    pcb_level_category: str = Field(
        ...,
        description="The category of total PCB levels, e.g., '>=0.430' or '<0.430'.",
    )
    genotype: str = Field(
        ..., description="The CYP1A1 M3 genotype status, e.g., 'Non-M3' or 'Any M3'."
    )
    patients_controls: str = Field(
        ...,
        description="The count of patients versus controls in the format 'patients/controls'.",
    )
    odds_ratio: Optional[Decimal] = Field(
        None, description="The calculated odds ratio for the specific group."
    )
    confidence_interval: Optional[str] = Field(
        None,
        description="The 95% confidence interval range as a string, e.g., '(0.8-3.2)'.",
    )


class BreastCancerRiskReport(BaseModel):
    """A report containing a list of breast cancer risk data records."""

    records: List[BreastCancerRiskData] = Field(
        ..., description="A list of individual risk data entries."
    )
