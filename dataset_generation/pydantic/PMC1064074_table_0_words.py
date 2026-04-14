from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class KineticParameter(BaseModel):
    condition: str = Field(
        ...,
        description="The experimental condition: 'ND' for nondeprived or 'D' for serum-deprived.",
    )
    vmax: Decimal = Field(
        ..., description="The maximum velocity of the reaction in mmol/l H+/minute."
    )
    vmax_std_error: Decimal = Field(
        ..., description="The standard error of the Vmax measurement."
    )
    k_prime_h: Decimal = Field(..., description="The apparent K' for H+ in µmol/l.")
    k_prime_h_std_error: Decimal = Field(
        ..., description="The standard error of the K' for H+ measurement."
    )


class KineticDataList(BaseModel):
    parameters: List[KineticParameter] = Field(
        ..., description="A list of kinetic parameter records for specific conditions."
    )
