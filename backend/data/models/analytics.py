from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from backend.data.db import Base

class GenreAnalytics(Base):
    __tablename__ = "genre_analytics"

    genre = Column(String, primary_key=True)
    
    click_count = Column(Integer, nullable=False, default=0)
    purchase_count = Column(Integer, nullable=False, default=0)

