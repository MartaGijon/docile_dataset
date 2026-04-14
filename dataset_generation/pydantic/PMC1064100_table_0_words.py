from typing import List
from pydantic import BaseModel, Field


class GenotypeCount(BaseModel):
    """Represents a specific genotype count for a family member category."""

    genotype: str = Field(
        ..., description="The specific genotype variant, e.g., 'CC', 'CT'."
    )
    affected_daughters: int = Field(
        ..., description="The number of affected daughters with this genotype."
    )
    unaffected_sons: int = Field(
        ..., description="The number of unaffected sons with this genotype."
    )


class GenotypeReport(BaseModel):
    """A report containing a list of genotype counts."""

    records: List[GenotypeCount] = Field(
        ..., description="List of genotype distribution records."
    )
