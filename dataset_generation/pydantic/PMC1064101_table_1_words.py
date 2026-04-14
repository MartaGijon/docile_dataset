from pydantic import BaseModel, Field
from decimal import Decimal


class HistologyFeature(BaseModel):
    """Represents a specific histology feature with its statistical data for a genetic group."""

    histology_type: str = Field(
        ..., description="The type of carcinoma, e.g., 'Ca ductale' or 'Ca lobulare'."
    )
    genetic_group: str = Field(
        ..., description="The genetic classification group, e.g., 'BRCA1' or 'BRCA2'."
    )
    count: int = Field(
        ..., description="The absolute number of cases observed in this group."
    )
    percentage: Decimal = Field(
        ...,
        description="The frequency percentage of this histology type within the group.",
    )


class HistologyAnalysisResult(BaseModel):
    """Container for a list of histology feature records."""

    features: list[HistologyFeature] = Field(
        ..., description="A list of histology feature records for the queried groups."
    )
