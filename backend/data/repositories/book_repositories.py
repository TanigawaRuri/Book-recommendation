from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.data.models.book import Book

def get_book_genre(db: Session, book_id: int):
    book = (
        db.query(Book.genre)
        .filter(Book.id == book_id)
        .scalar()
    )

    return book if book else None

def get_random_books(db: Session, k: int, recommended_ids: set):
    books = (
        db.query(Book)
        .filter(~Book.id.in_(recommended_ids))
        .order_by(func.random())
        .limit(k)
        .all()
    )
    return books