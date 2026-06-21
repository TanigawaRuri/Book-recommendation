from sqlalchemy.orm import Session
from backend.models.user import User, Userlogin
from backend.data.repositories import user_repositories as user_repo
from backend.utils.security import hash_password, verify_password


def signup(db: Session, user: User):
    username = user.username
    email = user.email
    password_hash = hash_password(user.password)

    return user_repo.create_user(db=db, username=username, email=email, password_hash=password_hash)

def login(user: Userlogin, db: Session):
    email = user.email
    password = user.password
    db_user = user_repo.get_user_by_email(db, email)
    if db_user is None:
        return None

    if not verify_password(password, db_user.password_hash):
        return None
    
    return db_user