from typing import List, Optional
from pydantic import BaseModel, Field


class StudyCriteria(BaseModel):
    """Represents a specific inclusion or exclusion criterion for a medical study."""

    category: str = Field(
        ...,
        description="The category of the criterion, either 'Inclusion' or 'Exclusion'.",
    )
    criterion_text: str = Field(
        ..., description="The full text description of the specific criterion."
    )
    relevant_field: Optional[str] = Field(
        None,
        description="The specific medical field or condition addressed, e.g., 'Age', 'Sex', 'Pregnancy'.",
    )


class StudyCriteriaList(BaseModel):
    """A container for a list of study criteria."""

    criteria: List[StudyCriteria] = Field(
        ..., description="A list of specific inclusion and exclusion criteria."
    )
