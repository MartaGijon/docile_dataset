from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class BreastCancerRiskData(BaseModel):
    """Represents a single row of breast cancer risk data from the study."""

    population_group: str = Field(
        ..., description="The demographic group, e.g., 'African Americans' or 'Whites'."
    )
    pcb_level: str = Field(
        ..., description="The PCB exposure level category, e.g., '<0.430' or '≥0.430'."
    )
    genotype: str = Field(
        ..., description="The CYP1A1 genotype status, e.g., 'Non-M1' or 'Any M1'."
    )
    patients_controls: str = Field(
        ..., description="The ratio of patients to controls in the format 'X/Y'."
    )
    odds_ratio: Optional[Decimal] = Field(
        None, description="The calculated odds ratio for the group. None if 'Referent'."
    )
    confidence_interval: Optional[str] = Field(
        None,
        description="The 95% confidence interval range as a string, e.g., '(0.9-2.5)'. None if 'Referent'.",
    )
    menopausal_status: str = Field(
        ...,
        description="The menopausal status of the subgroup, e.g., 'All participants', 'Premenopausal', or 'Postmenopausal'.",
    )


class BreastCancerRiskDataset(BaseModel):
    """Container for a list of breast cancer risk data records."""

    records: List[BreastCancerRiskData] = Field(
        ..., description="A list of individual risk data entries."
    )
