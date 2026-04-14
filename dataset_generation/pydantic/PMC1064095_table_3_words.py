from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class PostmenopausalPCBData(BaseModel):
    """Data for postmenopausal women regarding PCB exposure and CYP1A1 M4 genotype."""

    pcb_level: str = Field(
        ..., description="Total PCB level category (e.g., '>=0.349')."
    )
    genotype: str = Field(
        ..., description="CYP1A1 M4 genotype status (e.g., 'Any M4')."
    )
    patients_controls: str = Field(
        ..., description="Ratio of patients to controls in the group."
    )
    odds_ratio: Optional[Decimal] = Field(
        None, description="Odds ratio for the group compared to referent."
    )
    confidence_interval: Optional[str] = Field(
        None, description="95% confidence interval for the odds ratio."
    )


class PostmenopausalPCBDataList(BaseModel):
    """A list of postmenopausal PCB data records."""

    records: List[PostmenopausalPCBData] = Field(
        ..., description="List of data records for postmenopausal women."
    )
