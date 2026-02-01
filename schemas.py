from pydantic import BaseModel, Field
from typing import List

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=10, description="The raw text to analyze")

    class Config:
        json_schema_extra = {
            "example": {
                "text": "FastAPI is amazing for building AI products quickly. I love how fast it is."
            }
        }

class AnalyzeResponse(BaseModel):
    sentiment: str
    polarity_score: float
    keywords: List[str]