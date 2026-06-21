from sqlalchemy.orm import Session
from backend.data.models.event import Event
from backend.data.models.book import Book
from backend.data.models.analytics import GenreAnalytics

from backend.data.repositories.book_repositories import get_book_genre

def insert_event(db: Session, user_id: int, book_id: int, event_type: str):
    event = Event(
        user_id = user_id,
        book_id = book_id,
        event_type = event_type
    )

    try:
        db.add(event)
    except Exception as e:
        print(e)
        db.rollback()
        raise

    return event

def update_genre_analytics(db: Session, book_id: int, event_type: str):
    genre = get_book_genre(db, book_id)

    analytics = (
        db.query(GenreAnalytics)
        .filter(GenreAnalytics.genre == genre)
        .first()
    )

    if analytics is None:
        analytics = GenreAnalytics(
            genre=genre,
            click_count=0,
            purchase_count=0
        )
        db.add(analytics)
    
    if event_type == "click":
        analytics.click_count += 1
    
    elif event_type == "purchase":
        analytics.purchase_count += 1
