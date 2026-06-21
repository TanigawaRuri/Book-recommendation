from fastapi import APIRouter
from fastapi.responses import FileResponse
from backend.models.user import User
from backend.service import user as service

router = APIRouter(prefix='/auth')

@router.get("/")
def signup_page():
    return FileResponse("frontend/index.html")
