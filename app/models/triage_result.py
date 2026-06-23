from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from app.database.database import Base


class TriageResult(Base):

    __tablename__ = "triage_results"

    id = Column(
        Integer,
        primary_key=True
    )

    message_id = Column(
        Integer,
        ForeignKey("messages.id")
    )

    category = Column(
        String
    )

    priority = Column(
        String
    )

    summary = Column(
        Text
    )

    suggested_action = Column(
        Text
    )

    confidence = Column(
        Float
    )

    needs_human = Column(
        Boolean
    )