from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class FibroblastIGFData(BaseModel):
    cell_type: str = Field(
        ..., description="The type of fibroblast cell line, either 'NAF' or 'CAF'."
    )
    sample_id: str = Field(
        ...,
        description="The specific identifier for the fibroblast sample (e.g., 'NAF-1', 'CAF-2').",
    )
    igf_ii_level: Decimal = Field(
        ...,
        description="The measured IGF II level in ng/µg for the monoculture condition.",
    )
    igf_ii_mean: Decimal = Field(
        ...,
        description="The mean IGF II level in ng/µg for the co-culture condition with MCF10AT cells.",
    )


class FibroblastIGFDataList(BaseModel):
    data: List[FibroblastIGFData] = Field(
        ..., description="A list of IGF II measurements for fibroblast samples."
    )
