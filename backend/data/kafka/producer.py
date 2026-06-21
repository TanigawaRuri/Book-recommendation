from confluent_kafka import Producer
import json

producer = Producer({
    "bootstrap.servers": "kafka:9092"
})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(
            f"Message delivered to"
            f"{msg.topic()} [{msg.partition()}]"
        )

def send_purchase_event(user_id: int, book_id: int):
    event = {
        "event_type": "purchase",
        "user_id": user_id,
        "book_id": book_id
    }

    producer.produce(
        topic="book-events",
        value=json.dumps(event),
        callback=delivery_report
    )
    
    producer.poll(0)