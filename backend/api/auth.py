from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from backend.models.user import User, Userlogin
from backend.service import user as service
from backend.data.db import get_db

router = APIRouter(prefix='/api/auth')

@router.post("/signup")
def sign_up(user: User, db: Session = Depends(get_db)):
    return service.signup(db, user)

@router.post("/login")
def login(request: Request, user: Userlogin, db: Session = Depends(get_db)):
    db_user = service.login(user, db)
    if db_user == None:
        raise HTTPException(status_code=401,
                            detail="Invalid credentials")
    
    request.session["user_id"] = db_user.id
    return {"message": "success", "session": request.session["user_id"]}