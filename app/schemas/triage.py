from pydantic import BaseModel


class TriageResponse(BaseModel):
    category: str
    priority: str
    confidence: float
    needs_human: bool