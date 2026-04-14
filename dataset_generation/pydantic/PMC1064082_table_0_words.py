from typing import List
from pydantic import BaseModel, Field


class LPA2ExpressionCount(BaseModel):
    expression_level: str = Field(
        ..., description="The level of LPA2 expression, either 'Low' or 'High'"
    )
    case_count: int = Field(
        ...,
        description="The number of cases observed for the specific expression level",
    )
    threshold_group: str = Field(
        ..., description="The group identifier based on the threshold, e.g., '>3000'"
    )


class LPA2ExpressionCountsList(BaseModel):
    records: List[LPA2ExpressionCount] = Field(
        ...,
        description="A list of records containing expression levels and their corresponding case counts",
    )
