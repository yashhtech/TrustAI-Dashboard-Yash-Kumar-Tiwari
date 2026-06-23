from pydantic import BaseModel


class ReviewDecision(BaseModel):

    id: int

    category: str

    priority: str