from confluent_kafka import Consumer
from backend.data.repositories.event_repositories import insert_event, update_genre_analytics
from backend.data.db import SessionLocal
import json

consumer = Consumer({
    "bootstrap.servers": "kafka:9092",
    "group.id": "bookstore-group",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["book-events"])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer 오류 메시지: {}".format(msg.error()))
        continue
    
    raw = msg.value().decode("utf-8")
    try:
        event = json.loads(raw)
    except json.JSONDecodeError:
        print("Not JSON:", raw)
        continue

    print("수신된 메시지: {}".format(event))
    
    db = SessionLocal()

    try:
        insert_event(
            db=db,
            user_id=event["user_id"],
            book_id=event["book_id"],
            event_type=event["event_type"]
        )

        update_genre_analytics(
            db=db,
            book_id=event["book_id"],
            event_type=event["event_type"]
        )

        db.commit()

    except Exception as e:
        print(e)
        db.rollback()

    finally:
        db.close()