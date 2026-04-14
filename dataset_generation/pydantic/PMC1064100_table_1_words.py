from typing import List
from pydantic import BaseModel, Field


class FamilyDistribution(BaseModel):
    """Represents a single row of family distribution data based on genetic variants."""

    gene_variant: str = Field(
        ...,
        description="The specific gene and variant allele combination, e.g., 'CYP17 1/0'.",
    )
    mother_status: str = Field(
        ...,
        description="The carrier status of the mother (Carrier, Non-carrier, Unknown).",
    )
    father_status: str = Field(
        ...,
        description="The carrier status of the father (Carrier, Non-carrier, Unknown).",
    )
    affected_daughters: int = Field(
        ..., description="The number of daughters affected by the condition."
    )
    unaffected_daughters: int = Field(
        ..., description="The number of daughters unaffected by the condition."
    )
    total_daughters: int = Field(
        ..., description="The total number of daughters in this category."
    )


class FamilyDistributionList(BaseModel):
    """Container for a list of family distribution records."""

    records: List[FamilyDistribution] = Field(
        ..., description="A list of family distribution entries."
    )
