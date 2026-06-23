from pydantic import BaseModel


class MessageCreate(BaseModel):
    raw_message: str