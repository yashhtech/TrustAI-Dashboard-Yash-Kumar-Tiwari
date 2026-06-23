from app.database.database import SessionLocal

from app.models.message import Message
from app.models.triage_result import TriageResult
from app.models.audit_log import AuditLog


class PersistenceService:

    @staticmethod
    def save(
        original_message,
        cleaned_message,
        translated_message,
        language,
        result
    ):

        db = SessionLocal()

        try:

            message = Message(
                raw_message=original_message,
                cleaned_message=cleaned_message,
                translated_message=translated_message,
                language=language
            )

            db.add(message)

            db.commit()

            db.refresh(message)

            triage = TriageResult(
                message_id=message.id,
                category=result["category"],
                priority=result["priority"],
                summary=result["summary"],
                suggested_action=result["suggested_action"],
                confidence=result["confidence"],
                needs_human=result["needs_human"]
            )

            db.add(triage)

            audit = AuditLog(
                event="AI_TRIAGE_COMPLETED",
                details=f"Message ID {message.id}"
            )

            db.add(audit)

            db.commit()

            return message.id

        finally:

            db.close()