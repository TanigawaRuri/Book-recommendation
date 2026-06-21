from backend.data.db import Base, engine

from backend.data.models.book import Book
from backend.data.models.user import User
from backend.data.models.event import Event
from backend.data.models.recommendation import Recommendation
from backend.data.models.analytics import GenreAnalytics

with engine.connect() as conn:
    result = conn.exec_driver_sql("SELECT current_user;")
    print(result.fetchone())

Base.metadata.create_all(bind=engine)