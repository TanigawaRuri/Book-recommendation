from apscheduler.schedulers.background import BackgroundScheduler

from backend.data.db import SessionLocal
from backend.data.repositories.recommendation_repositories import update_recommendation
from backend.data.models.user import User

def recommendation_job():
    db = SessionLocal()

    try:
        users = db.query(User).all()

        for user in users:
            update_recommendation(
                db,
                user.id
            )
        
        print("recommendations updated")
    
    finally:
        db.close()
    
scheduler = BackgroundScheduler()
scheduler.add_job(
    recommendation_job,
    trigger="interval",
    minutes=10
)