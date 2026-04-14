from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class NodeMortalityData(BaseModel):
    """Represents a single row of node involvement and mortality statistics."""

    involved_nodes_range: str = Field(
        ...,
        description="The range of pathologically involved axillary lymph nodes (e.g., '11-20').",
    )
    patients_at_risk: int = Field(
        ...,
        description="The total number of patients at risk within this node involvement range.",
    )
    breast_cancer_mortality_pct: Decimal = Field(
        ...,
        description="The unadjusted breast cancer mortality rate as a percentage for this group.",
    )


class NodeMortalityReport(BaseModel):
    """Container for a list of node mortality data records."""

    records: List[NodeMortalityData] = Field(
        ...,
        description="A list of mortality statistics grouped by involved node ranges.",
    )
