from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field


class SampleData(BaseModel):
    """Represents a single biological sample measurement."""

    sample_id: str = Field(
        ..., description="The unique identifier for the sample, e.g., 'NAF-1'."
    )
    cell_type: str = Field(
        ..., description="The category of the cell type, e.g., 'NAF' or 'CAF'."
    )
    igf_ii_level: Decimal = Field(
        ...,
        description="The measured IGF II level normalized to total protein in ng/µg.",
    )
    mean_igf_ii_level: Optional[Decimal] = Field(
        None, description="The mean IGF II level for the group if available, in ng/µg."
    )


class SampleDataList(BaseModel):
    """Container for a list of sample data entries."""

    samples: List[SampleData] = Field(
        ..., description="A list of individual sample measurements."
    )
