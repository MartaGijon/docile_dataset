from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field


class RadiotracerMetric(BaseModel):
    """Represents a specific performance metric for a radiotracer in a defined patient subgroup."""

    radiotracer_name: str = Field(
        ..., description="The name of the radiotracer, e.g., '99mTc-(V)DMSA'."
    )
    patient_subgroup: str = Field(
        ..., description="The specific patient cohort, e.g., 'Head-to-head patients'."
    )
    metric_type: str = Field(
        ...,
        description="The type of statistical metric, e.g., 'Sensitivity' or 'Specificity'.",
    )
    value_percentage: Decimal = Field(
        ..., description="The numerical value of the metric as a percentage."
    )


class RadiotracerMetricsList(BaseModel):
    """A container for a list of radiotracer performance metrics."""

    metrics: List[RadiotracerMetric] = Field(
        ..., description="A list of RadiotracerMetric objects."
    )
