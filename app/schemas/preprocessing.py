from pydantic import BaseModel
from typing import List


class PreprocessingResponse(BaseModel):

    original_text: str

    cleaned_text: str

    language: str

    translated_text: str

    pii_detected: List[str]

    contains_code: bool

    prompt_injection: bool

    garbage_input: bool