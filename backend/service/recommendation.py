from sqlalchemy.orm import Session
from backend.data.repositories import user_repositories as user_repo
from backend.data.repositories import recommendation_repositories as recommendation_repo

def get_recommended_books(db: Session, user_id: int, k=3):
    recommended_books = recommendation_repo.recommend_by_id(db, user_id, k)
    if recommended_books is None:
        return None
    return recommended_books