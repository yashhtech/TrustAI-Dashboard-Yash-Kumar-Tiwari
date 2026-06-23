from pydantic import BaseModel


class TriageAIResponse(BaseModel):

    category: str

    priority: str

    summary: str

    suggested_action: str

    needs_human: bool

    confidence: float