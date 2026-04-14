from pydantic import BaseModel, Field
from decimal import Decimal


class CellCultureIndex(BaseModel):
    """Represents the BrdU-labeling index data for a specific cell culture condition."""

    culture_group: str = Field(
        ...,
        description="The name of the culture group, e.g., 'NAF-1 + MCF10A' or 'CAF-1 + MCF10A'.",
    )
    sample_size: int = Field(
        ...,
        description="The number of samples (n) used for this specific culture group.",
    )
    mean_index: Decimal = Field(
        ..., description="The mean BrdU-labeling index for the group."
    )
    standard_error: Decimal = Field(
        ..., description="The standard error of the mean BrdU-labeling index."
    )


class CellCultureIndexList(BaseModel):
    """A container for a list of cell culture index records."""

    records: list[CellCultureIndex] = Field(
        ..., description="A list of CellCultureIndex objects."
    )
