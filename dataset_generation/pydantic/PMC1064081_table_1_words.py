from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class PatientRiskData(BaseModel):
    """Represents a single row of patient risk and mortality data."""

    log_odds_range: str = Field(
        ...,
        description="The range of the estimated log odds of nodal involvement (e.g., '-3 < L <= -2').",
    )
    number_of_patients: int = Field(
        ...,
        description="The total number of patients at risk within this log odds range.",
    )
    breast_cancer_mortality_rate: Decimal = Field(
        ...,
        description="The unadjusted breast cancer mortality rate for this group, expressed as a percentage.",
    )


class PatientRiskDataList(BaseModel):
    """Container for a list of patient risk data records."""

    records: List[PatientRiskData] = Field(
        ..., description="A list of patient risk and mortality records."
    )
