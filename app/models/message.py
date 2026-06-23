from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class Message(Base):

    __tablename__ = "messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    raw_message = Column(
        Text,
        nullable=False
    )

    cleaned_message = Column(
        Text,
        nullable=True
    )

    translated_message = Column(
        Text,
        nullable=True
    )

    language = Column(
        Text,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )