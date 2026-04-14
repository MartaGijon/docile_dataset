from pydantic import BaseModel, Field
from decimal import Decimal


class VariantRiskData(BaseModel):
    variant_name: str = Field(
        ...,
        description="The specific name of the CHEK2 genetic variant (e.g., 1100delC, I175T).",
    )
    carrier_status: str = Field(
        ...,
        description="Indicates whether the subject is a carrier or non-carrier of the variant.",
    )
    case_count: int = Field(
        ...,
        description="The number of breast cancer cases observed for this specific variant and carrier status.",
    )
    odds_ratio: Decimal = Field(
        ...,
        description="The calculated odds ratio representing the risk association, stored as a Decimal for precision.",
    )


VariantRiskDataList = list[VariantRiskData]
