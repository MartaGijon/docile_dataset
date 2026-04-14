from typing import List
from pydantic import BaseModel, Field


class TumorPairData(BaseModel):
    """Represents a single row of tumor pair analysis data."""

    carcinoma_status: str = Field(
        ..., description="Status of the carcinoma sample (e.g., 'Carcinoma+')"
    )
    nipple_status: str = Field(
        ..., description="Status of the nipple sample (e.g., 'nipple-')"
    )
    pair_count: int = Field(
        ..., description="The number of tumor pairs matching this configuration"
    )
    hpv_types: List[str] = Field(
        default_factory=list,
        description="List of specific HPV types identified in these pairs",
    )


class TumorPairAnalysisResult(BaseModel):
    """Container for a list of tumor pair analysis records."""

    records: List[TumorPairData] = Field(
        ..., description="List of tumor pair data entries"
    )
