from sqlalchemy.orm import Session
from backend.data.repositories import event_repositories as event_repo

def add_event_log(db: Session, user_id: int, book_id: int, event_type: str):
    return event_repo.insert_event(db, user_id, book_id, event_type)