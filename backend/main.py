import uvicorn
import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from backend.api.auth import router as api_auth_router
from backend.api.recommendation import router as api_recommendation_router
from backend.api.event import router as api_event_router
from backend.web.auth import router as web_auth_router
from backend.web.recommendation import router as web_recommendation_router
from backend.data.db import Base, engine

from contextlib import asynccontextmanager
from backend.scheduler.recommendation_scheduler import scheduler

@asynccontextmanager
async def lifespan(app: FastAPI):
    for _ in range(10):
        try:
            Base.metadata.create_all(bind=engine)
            break

        except Exception:
            time.sleep(2)

    scheduler.start()
    print("scheduler started")

    yield

    scheduler.shutdown()

app = FastAPI(
    lifespan=lifespan
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

app.add_middleware(
    SessionMiddleware,
    secret_key="some-secret-key"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(web_auth_router)
app.include_router(web_recommendation_router)

app.include_router(api_auth_router)
app.include_router(api_recommendation_router)
app.include_router(api_event_router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)