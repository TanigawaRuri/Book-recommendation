from sqlalchemy.orm import Session
from backend.data.models.user import User

def create_user(db: Session, username: str, email: str, password_hash:str):
    user = User(
        username=username,
        email=email,
        password_hash=password_hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

