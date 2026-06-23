from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from datetime import datetime

from app.database.database import Base


class ReviewQueue(Base):
    __tablename__ = "review_queue"

    id = Column(Integer, primary_key=True)

    message = Column(String)

    ai_category = Column(String)

    ai_priority = Column(String)

    ai_confidence = Column(String)

    status = Column(
        String,
        default="pending"
    )

    reviewed = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )