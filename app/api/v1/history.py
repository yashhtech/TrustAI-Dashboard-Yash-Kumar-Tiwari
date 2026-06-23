from fastapi import APIRouter

from app.database.database import SessionLocal

from app.models.message import Message
from app.models.triage_result import TriageResult

router = APIRouter()


@router.get("/history")
def history():

    db = SessionLocal()

    try:

        messages = db.query(
            Message
        ).all()

        result = []

        for message in messages:

            triage = db.query(
                TriageResult
            ).filter(
                TriageResult.message_id == message.id
            ).first()

            result.append({
                "id": message.id,
                "message": message.raw_message,
                "language": message.language,
                "category": triage.category if triage else None,
                "priority": triage.priority if triage else None,
                "confidence": triage.confidence if triage else None
            })

        return result

    finally:
        db.close()