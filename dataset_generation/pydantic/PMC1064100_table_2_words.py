from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class GeneticAssociationRecord(BaseModel):
    """Represents a single genetic association data point for a specific variant and model."""

    variant_allele: str = Field(
        ...,
        description="The specific variant allele identifier, e.g., 'C' or '(TTTA)11'.",
    )
    estimated_frequency_percent: Decimal = Field(
        ...,
        description="The estimated frequency of the allele expressed as a percentage.",
    )
    p_value: Decimal = Field(
        ...,
        description="The P-value derived from the one-tailed test statistics for the association.",
    )


class GeneticAssociationReport(BaseModel):
    """A container for a list of genetic association records."""

    records: List[GeneticAssociationRecord] = Field(
        ...,
        description="A list of genetic association records matching the query criteria.",
    )
