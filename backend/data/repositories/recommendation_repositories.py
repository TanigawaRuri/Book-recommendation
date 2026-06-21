from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.data.models.recommendation import Recommendation
from backend.data.models.book import Book
from backend.data.models.event import Event

from backend.data.repositories.book_repositories import get_random_books

def recommend_by_id(db: Session, user_id: int, k: int):
    rows = (
        db.query(Book.id, Book.title)
        .join(
            Recommendation,
            Recommendation.book_id == Book.id
        )
        .filter(Recommendation.user_id == user_id)
        .order_by(Recommendation.rank)
        .limit(k)
        .all()
    )

    recommendations = []

    for row in rows:
        recommendations.append({
            "user_id": user_id,
            "id": row.id,
            "title": row.title
        })
    
    remaining = k - len(recommendations)
    
    if remaining:
        recommended_ids = {r["id"] for r in recommendations}

        random_books = get_random_books(db, remaining, recommended_ids)

        recommendations.extend(
            {
                "user_id": user_id,
                "id": book.id,
                "title": book.title
            }
            for book in random_books
        )

    return {"recommendations": recommendations}

def generate_recommendations(db: Session, user_id: int):
    ranked = (
        db.query(Event.user_id,
                 Event.book_id,
                 func.count().label("cnt"),
                 func.row_number()
                    .over(
                        partition_by=Event.user_id,
                        order_by=func.count().desc()
                    )
                    .label("rn")
        )
        .group_by(Event.user_id, Event.book_id)
        .cte("ranked")
    )

    favorite_book = (
        db.query(ranked.c.book_id)
        .filter(
            ranked.c.rn == 1,
            ranked.c.user_id == user_id
        )
        .scalar()
    )

    favorite_users = (
        db.query(ranked.c.user_id)
        .filter(
            ranked.c.rn == 1,
            ranked.c.book_id == favorite_book
        )
    )

    query = (
        db.query(ranked.c.book_id, func.count().label("score"))
        .filter(
            ranked.c.rn == 2,
            ranked.c.user_id.in_(favorite_users)
        )
        .group_by(ranked.c.book_id)
        .order_by(func.count().desc())
        .limit(3)
        .all()
    )

    return query

def save_recommendations(db: Session, user_id: int, recommendations):
    db.query(Recommendation).filter(
            Recommendation.user_id == user_id
        ).delete()

    for rank, (book_id, score) in enumerate(
        recommendations,
        start=1
    ):
        db.add(
            Recommendation(
                user_id=user_id,
                book_id=book_id,
                rank=rank
            )
        )

    db.commit()

def update_recommendation(db, user_id):
    recommendations = generate_recommendations(
        db,
        user_id
    )

    save_recommendations(
        db,
        user_id,
        recommendations
    )