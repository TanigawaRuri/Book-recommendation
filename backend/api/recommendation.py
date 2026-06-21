from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.service import recommendation as service
from backend.data.db import get_db

router = APIRouter(prefix="/api/recommendation")

@router.get("")
@router.get("/")
def recommendation(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    
    if user_id is None:
        raise HTTPException(401, "Please login")
    
    return service.get_recommended_books(db, user_id)
    