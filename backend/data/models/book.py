from sqlalchemy import Column, Integer, String
from backend.data.db import Base

class Book(Base):
    __tablename__ =  "books"
    
    id = Column(Integer, primary_key=True)
    ncode = Column(String, unique=True, nullable=False, index=True)
    title = Column(String(500), nullable=False)
    author = Column(String(100), nullable=False)
    year = Column(Integer)

    genre = Column(String(20), nullable=False)