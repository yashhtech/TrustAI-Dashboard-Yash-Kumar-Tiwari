from fastapi import APIRouter

from app.schemas.message import MessageCreate
from app.schemas.preprocessing import PreprocessingResponse

from app.services.preprocessor import Preprocessor
from app.services.pii_detector import PIIDetector
from app.services.code_detector import CodeDetector
from app.services.prompt_injection import PromptInjectionDetector
from app.services.garbage_detector import GarbageDetector

router = APIRouter()


@router.post("/preprocess", response_model=PreprocessingResponse)
def preprocess_message(payload: MessageCreate):

    cleaned = Preprocessor.clean_text(
        payload.raw_message
    )

    language = Preprocessor.detect_language(
        cleaned
    )

    translated = Preprocessor.translate_to_english(
        cleaned,
        language
    )

    pii = PIIDetector.detect(
        cleaned
    )

    code = CodeDetector.detect(
        cleaned
    )

    injection = PromptInjectionDetector.detect(
        cleaned
    )

    garbage = GarbageDetector.detect(
        cleaned
    )

    return {
        "original_text": payload.raw_message,
        "cleaned_text": cleaned,
        "language": language,
        "translated_text": translated,
        "pii_detected": pii,
        "contains_code": code,
        "prompt_injection": injection,
        "garbage_input": garbage
    }