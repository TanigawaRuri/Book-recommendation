from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from backend.data.db import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    book_id = Column(Integer, nullable=False)
    event_type = Column(String(20), nullable=False)
    event_time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    