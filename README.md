# Event-Driven Book Recommendation System

## Overview

This project is an event-driven book recommendation platform built with FastAPI, PostgreSQL, Kafka, and Docker.

The system imports book data from the Narou Novel API, stores it in PostgreSQL, and processes user interactions asynchronously through Kafka. User events such as purchases are consumed by a background worker that updates recommendation and analytics data.

The goal of the project is to demonstrate practical Data Engineering concepts including data ingestion, event streaming, asynchronous processing, database design, and containerized deployment.

---

## Architecture

```text
Narou API
    │
    ▼
Book Import Pipeline
    │
    ▼
PostgreSQL
 ┌──────────────────┐
 │ Users            │
 │ Books            │
 │ Recommendations  │
 │ Analytics        │
 └──────────────────┘
          ▲
          │
       FastAPI
          │
          ▼
      User Events
          │
          ▼
        Kafka
          │
          ▼
       Consumer
      ├─────────────► Analytics Update
      └─────────────► Recommendation Update
```

---

## Features

### Authentication

* User registration
* User login
* Password hashing using bcrypt
* JWT-based authentication

### Book Catalog

* Book metadata imported from the Narou API
* PostgreSQL storage and querying

### Recommendation System

* Recommendation records stored in PostgreSQL
* Recommendations retrieved through API endpoints
* Recommendation updates processed asynchronously

### Event-Driven Processing

* Purchase events published to Kafka
* Kafka consumer processes events independently
* Analytics and recommendation tables updated asynchronously

### Containerized Deployment

* PostgreSQL
* Kafka
* FastAPI Backend
* Kafka Consumer

All services can be started with Docker Compose.

---

## Technology Stack

| Category         | Technology             |
| ---------------- | ---------------------- |
| Backend          | FastAPI                |
| Database         | PostgreSQL             |
| Streaming        | Kafka                  |
| ORM              | SQLAlchemy             |
| Authentication   | JWT, bcrypt            |
| Containerization | Docker, Docker Compose |
| Data Source      | Narou Novel API        |

---

## Database Design

Core tables:

### Users

Stores user account information.

### Books

Stores imported book metadata.

### Recommendations

Stores personalized recommendation rankings.

### Analytics

Stores aggregated interaction statistics.

---

## Data Flow

### Purchase Event Pipeline

```text
User Purchase
      │
      ▼
FastAPI Endpoint
      │
      ▼
Kafka Producer
      │
      ▼
Kafka Topic
      │
      ▼
Kafka Consumer
      │
      ├────► Analytics Update
      │
      └────► Recommendation Update
```

This design decouples API requests from downstream processing and allows analytics and recommendation logic to scale independently.

---

## Challenges

### Kafka Startup Ordering

Containers may start before Kafka is fully available.

**Solution**

* Added Kafka health checks
* Configured service dependencies to wait for Kafka readiness

### PostgreSQL Persistence

Container recreation can lead to data loss if storage is not persisted.

**Solution**

* Configured named Docker volumes for PostgreSQL

### Asynchronous Recommendation Processing

Updating recommendation data directly in API requests increases coupling.

**Solution**

* Implemented Kafka-based event processing
* Moved recommendation and analytics updates to consumer services

---

## Running the Project

### Start Services

```bash
docker compose up --build
```

### Available Services

| Service    | Port |
| ---------- | ---- |
| FastAPI    | 8000 |
| PostgreSQL | 5432 |
| Kafka      | 9092 |

### API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Screenshots

### Login

[Insert Screenshot]

### Recommendation Page

[Insert Screenshot]

### Swagger API Documentation

[Insert Screenshot]

---

## Future Improvements

* Collaborative filtering recommendation engine
* Kafka consumer groups
* Dead letter queue handling
* Automated ETL scheduling
* Cloud deployment
* Monitoring and observability

---

## Learning Outcomes

Through this project I gained experience with:

* Event-driven architectures
* Kafka producers and consumers
* PostgreSQL schema design
* Dockerized application deployment
* API development using FastAPI
* Asynchronous data processing
* Recommendation system implementation

```
```
