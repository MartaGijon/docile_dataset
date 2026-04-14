from typing import List
from pydantic import BaseModel, Field


class MaternalAgeExposureData(BaseModel):
    """Represents a single row of data for maternal age and birth order exposure."""

    dataset_name: str = Field(
        ..., description="The name of the dataset, e.g., 'Maternal age dataset'."
    )
    exposure_type: str = Field(
        ...,
        description="The type of exposure being measured, e.g., 'Birth order' or 'Maternal age'.",
    )
    race_group: str = Field(
        ...,
        description="The racial group for the data, e.g., 'African-American' or 'White'.",
    )
    cases_count: int = Field(..., description="The number of cases in this group.")
    cases_percentage: float = Field(
        ..., description="The percentage of cases in this group."
    )
    controls_count: int = Field(
        ..., description="The number of controls in this group."
    )
    controls_percentage: float = Field(
        ..., description="The percentage of controls in this group."
    )


class MaternalAgeExposureList(BaseModel):
    """A list of maternal age and birth order exposure data records."""

    records: List[MaternalAgeExposureData] = Field(
        ..., description="A list of data records for the query."
    )
