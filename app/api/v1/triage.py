from fastapi import APIRouter
import time
from app.schemas.message import MessageCreate

from app.services.preprocessor import Preprocessor
from app.services.code_detector import CodeDetector

from app.services.ollama_service import OllamaService
from app.services.code_router import CodeRouter
from app.services.security_engine import SecurityEngine
from app.services.confidence_engine import ConfidenceEngine

from app.services.validators.category_validator import CategoryValidator
from app.services.validators.priority_validator import PriorityValidator
from app.services.persistence_service import PersistenceService
from app.services.review_service import ReviewService
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.session import get_db
from app.services.trust.trust_engine import TrustEngine
from app.services.trust.explainability_engine import ExplainabilityEngine
from app.services.trust.risk_engine import RiskEngine
from app.services.sentiment_engine import SentimentEngine



router = APIRouter()


@router.post("/triage")
def triage(
    payload: MessageCreate,
    db: Session = Depends(get_db)
):

    processed = Preprocessor.process(payload.raw_message)

    cleaned = processed["cleaned"]
    translated = processed["translated"]
    language = processed["language"]

    contains_code = CodeDetector.detect(
        cleaned
    )

    start = time.time()

    ai_result = OllamaService.classify(translated)

    end = time.time()

    ai_result["latency_ms"] = round((end - start) * 1000, 2)

    # simple token estimation
    tokens = len(cleaned.split())
    ai_result["tokens"] = tokens
    ai_result["estimated_cost"] = round(tokens * 0.00001, 5)

    ai_result["category"] = (
        CategoryValidator.validate(
            ai_result.get("category")
        )
    )

    ai_result["priority"] = (
        PriorityValidator.validate(
            ai_result.get("priority")
        )
    )

    ai_result = CodeRouter.route(
        contains_code,
        ai_result
    )

    ai_result = SecurityEngine.evaluate(
        cleaned,
        ai_result
    )

    ai_result = ConfidenceEngine.evaluate(
        ai_result
    )

    PersistenceService.save(
    original_message=payload.raw_message,
    cleaned_message=cleaned,
    translated_message=translated,
    language=language,
    result=ai_result
)
    
    if ai_result["confidence"] < 0.70:

        ReviewService.add_to_queue(
        db,
        payload.raw_message,
        ai_result["category"],
        ai_result["priority"],
        ai_result["confidence"]
    )
    ai_result["trust_score"] = (
       TrustEngine.calculate(
        ai_result
       )
     )

    ai_result["explanation"] = (
    ExplainabilityEngine.generate(
        cleaned,
        ai_result
    )
    )

    ai_result["risk_level"] = (
    RiskEngine.evaluate(
        ai_result
    )
     )
    
    ai_result["sentiment"] = (
    SentimentEngine.detect(
        cleaned
    )
     )

    return ai_result