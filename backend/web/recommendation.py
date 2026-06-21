from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix='/recommendation')

@router.get("")
@router.get("/")
def signup_page():
    return FileResponse("frontend/recommendation.html")