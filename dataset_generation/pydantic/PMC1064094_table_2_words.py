from typing import List
from pydantic import BaseModel, Field


class CarcinomaHPVData(BaseModel):
    """Represents a single row of carcinoma data filtered by HPV type and location."""

    carcinoma_type: str = Field(
        ...,
        description="The specific type of carcinoma, e.g., 'Intraductal', 'Lobular'.",
    )
    location: str = Field(
        ..., description="The anatomical location of the carcinoma, e.g., 'Nipple'."
    )
    hpv_type_11_count: int = Field(
        ..., description="The count of cases associated with HPV type 11."
    )
    hpv_type_16_count: int = Field(
        ..., description="The count of cases associated with HPV type 16."
    )


class CarcinomaHPVDataList(BaseModel):
    """A container for a list of carcinoma data entries."""

    data: List[CarcinomaHPVData] = Field(
        ..., description="A list of carcinoma records matching the query criteria."
    )
