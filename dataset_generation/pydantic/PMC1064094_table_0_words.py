from typing import List
from pydantic import BaseModel, Field


class CarcinomaData(BaseModel):
    carcinoma_type: str = Field(
        ...,
        description="The specific type of carcinoma, e.g., Invasive ductal, Medullary, Tubular.",
    )
    location: str = Field(
        ...,
        description="The anatomical location of the carcinoma, e.g., Carcinoma, Nipple.",
    )
    hpv_dna_positive_count: int = Field(
        ..., description="The count of samples testing positive for HPV DNA."
    )


class CarcinomaDataList(BaseModel):
    items: List[CarcinomaData] = Field(
        ...,
        description="A list of carcinoma data records filtered by the query criteria.",
    )
