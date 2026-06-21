from pydantic import BaseModel

class Event(BaseModel):
    book_id: int
    event_type: str = "click"