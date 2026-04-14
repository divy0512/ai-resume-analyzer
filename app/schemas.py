from pydantic import BaseModel
from typing import List

class ResumeAnalysis(BaseModel):
    match_score: int
    matched_keywords: List[str]
    missing_keywords: List[str]
    suggestions: List[str]
    overall_feedback: str
