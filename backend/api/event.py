from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from backend.data.kafka.producer import send_purchase_event

from backend.models.event import Event
from backend.service import event as service
from backend.data.db import get_db

router = APIRouter(prefix='/api/event')

@router.post("/purchase/")
@router.post("/purchase")
def add_event_log(event: Event, request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if user_id is None:
        raise HTTPException(401, "Please login")
    
    book_id = event.book_id
    #event_type = event.event_type
    
    send_purchase_event(user_id, book_id)

    #return service.add_event_log(db, user_id, book_id, event_type=event_type)