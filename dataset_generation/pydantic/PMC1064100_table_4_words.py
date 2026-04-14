from pydantic import BaseModel, Field
from decimal import Decimal


class VariantStatistic(BaseModel):
    variant_name: str = Field(
        ..., description="The name of the genetic variant, e.g., CYP19"
    )
    allele: str = Field(
        ..., description="The specific allele configuration, e.g., (TTTA)≥10"
    )
    model_type: str = Field(
        ..., description="The genetic model used for calculation, e.g., Additive"
    )
    mothers_test_statistic: Decimal = Field(
        ...,
        description="The test statistic value for mothers under the specified model",
    )
    mothers_p_value: Decimal = Field(
        ..., description="The P-value associated with the mothers' test statistic"
    )
    fathers_test_statistic: Decimal = Field(
        ...,
        description="The test statistic value for fathers under the specified model",
    )
    fathers_p_value: Decimal = Field(
        ..., description="The P-value associated with the fathers' test statistic"
    )


class VariantStatisticList(BaseModel):
    statistics: list[VariantStatistic] = Field(
        ..., description="A list of variant statistics matching the query criteria"
    )
