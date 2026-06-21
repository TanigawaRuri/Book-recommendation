from sqlalchemy.orm import Session

from backend.data.db import SessionLocal
from backend.data.models.book import Book
from data_pipeline.jobs.narou_books_ingestion import fetch_novels

def insert_book(db: Session):
    genre_info = {0: "未選択", 1: "恋愛", 2: "ファンタジー", 3: "文芸", 4: "SF", 99: "その他", 98: "ノンジャンル"}
    try:
        for i in range(1, 2001):
            data = fetch_novels(i)
            existing = db.query(Book).filter(
                Book.ncode == data["ncode"]
            ).first()

            if existing:
                continue
            
            biggenre = int(data["biggenre"])
            genre_info.get(biggenre, "その他")

            book = Book(
                title = data["title"],
                ncode = data["ncode"],
                author = data["writer"],
                year = int(data["general_firstup"].split("-")[0]),
                genre = genre_info.get(biggenre, "その他")
            )

            db.add(book)
            if i % 100 == 0:
                print(f"{i} processed")

        db.commit()
        print("success")

    except Exception as e:
        print(f"{i}: {e}")
        db.rollback()
        raise

db = SessionLocal()

try:
    insert_book(db)
finally:
    db.close()