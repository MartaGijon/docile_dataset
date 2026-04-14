from typing import List
from pydantic import BaseModel, Field


class PreMenopausalTumorSize(BaseModel):
    """Represents tumor size distribution for pre-menopausal patients."""

    tumor_stage: str = Field(
        ..., description="The tumor stage classification (e.g., T1, T2)."
    )
    patient_count: int = Field(
        ..., description="The number of patients in this specific tumor stage."
    )


class PreMenopausalTumorSizeList(BaseModel):
    """Container for a list of pre-menopausal tumor size records."""

    records: List[PreMenopausalTumorSize] = Field(
        ..., description="A list of tumor size statistics for pre-menopausal patients."
    )
