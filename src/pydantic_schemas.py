from pydantic import BaseModel, Field
from typing import Dict, Any


class Dataset_Generation(BaseModel):
    query: str = Field(..., description=" SQL query in text format")
    pydantic_model: str = Field(..., description="Pydantic model for the query")
    ground_truth_json: Dict[str, Any] = Field(
        ..., description="Ground truth JSON for the query"
    )
