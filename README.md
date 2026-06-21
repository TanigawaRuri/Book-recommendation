# Event-Driven Book Recommendation System

## Overview

This project is an event-driven book recommendation platform built with FastAPI, PostgreSQL, Kafka, and Docker.

The system imports book data from the Narou Novel API, stores it in PostgreSQL, and processes user interactions asynchronously through Kafka. User events such as purchases are consumed by a background worker that updates recommendation and analytics data.

The goal of the project is to demonstrate practical Data Engineering concepts including data ingestion, event streaming, asynchronous processing, database design, and containerized deployment.

---

## Architecture

<img width="690" height="800" alt="data_engineer_portfolio_architecture" src="https://github.com/user-attachments/assets/0f5515ac-7906-4a33-b6b8-1de45e7b43a1" />


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

## ERD

<img width="1231" height="631" alt="image" src="https://github.com/user-attachments/assets/e08abfb9-4da8-456d-b072-81e2deac698b" />


## Database Design

### Users

Stores user account information and authentication data.

| Column        | Description                  |
| ------------- | ---------------------------- |
| id            | Unique user identifier       |
| email         | User email address           |
| password_hash | Hashed password using bcrypt |

Used for authentication and personalization.

---

### Books

Stores book metadata imported from the Narou API.

| Column   | Description            |
| -------- | ---------------------- |
| id       | Unique book identifier |
| title    | Book title             |
| genre    | Book genre             |
| author   | Author name            |
| ncode | Book ncode       |

Acts as the primary catalog for recommendation and search operations.

---

### Recommendations

Stores personalized recommendation rankings for each user.

| Column  | Description             |
| ------- | ----------------------- |
| user_id | Target user             |
| book_id | Recommended book        |
| rank    | Recommendation priority |

Queried by the recommendation API to serve personalized book suggestions.

---

### GenreAnalytics

Stores aggregated user interaction statistics by genre.

| Column         | Description         |
| -------------- | ------------------- |
| genre          | Book genre          |
| click_count    | Number of clicks    |
| purchase_count | Number of purchases |

Used to track user engagement trends and support recommendation logic.

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

<img width="450" height="592" alt="image" src="https://github.com/user-attachments/assets/476071e1-ef9b-416e-8b84-7238b841a717" />


### Recommendation Page

<img width="891" height="499" alt="image" src="https://github.com/user-attachments/assets/9347d030-8553-4240-8633-11cb55ad16de" />


### Swagger API Documentation

<img width="439" height="582" alt="image" src="https://github.com/user-attachments/assets/64bb7e5b-7a55-4e90-8c99-c9848090fd1b" />


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

* Event-driven architectures
* Kafka producers and consumers
* PostgreSQL schema design
* Dockerized application deployment
* API development using FastAPI
* Asynchronous data processing
* Recommendation system implementation

```
```
