# 🏙️ Urban Flow Traffic API – Dockerized Smart City Backend

## 👤 Role
**The Architect (Docker & Orchestration)**  
**Name:** Ashwani Sharma  

---

## 📌 Project Overview

The **Urban Flow Traffic API** is a backend system designed to support smart city traffic management.  
It collects traffic data from multiple locations, calculates congestion levels, and exposes RESTful APIs for real-time monitoring and analysis.

Originally, the application suffered from **environment mismatch issues**, where it worked on one system but crashed on another due to dependency and configuration differences.

This project solves that problem by **fully containerizing the application and its dependencies** using Docker and Docker Compose.

---

## 🎯 Problem Statement

Developers faced frequent crashes due to:
- Different Python versions
- Missing libraries
- Database configuration inconsistencies
- Host-specific environment dependencies

---

## ✅ Solution Approach

To eliminate these issues:
- The application is containerized using **Docker**
- Multiple services are orchestrated using **Docker Compose**
- Databases and cache run as containers
- Resource limits are enforced to avoid system overload
- A single command starts the entire stack

---

## 🧱 Technology Stack

| Layer | Technology |
|-----|-----------|
| Backend API | FastAPI (Python) |
| Database | PostgreSQL (Docker Image) |
| Cache | Redis (Docker Image) |
| ORM | SQLAlchemy |
| API Server | Uvicorn |
| Containerization | Docker |
| Orchestration | Docker Compose |

---

## 🗂️ Project Structure
```bash
urban-flow-api/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── database.py # Database configuration
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # Business logic
│ └── routes/
│ └── traffic.py # API routes
│
├── Dockerfile # Multi-stage Docker build
├── docker-compose.yml # Service orchestration
├── requirements.txt # Python dependencies
├── .env # Environment variables
└── README.md # Documentation

```
---

## 🐳 Dockerfile Design (Multi-Stage Build)

### Key Features
- Uses `python:3.11-slim` for smaller image size
- Multi-stage build to separate build and runtime layers
- Non-root user execution for security
- Optimized image size (under 200MB)

### Benefits
- Faster builds
- Reduced attack surface
- Production-grade container image

---

## 🧱 Docker Compose Architecture

The application consists of **three containerized services**:

### 1️⃣ API Service
- Runs the FastAPI application
- Exposed on port `8000`
- Connects to PostgreSQL and Redis using internal Docker networking

### 2️⃣ PostgreSQL Service
- Uses official `postgres:15-alpine` image
- Runs entirely inside Docker
- Uses Docker volume for persistent data storage
- No PostgreSQL installation required on host machine

### 3️⃣ Redis Service
- Uses official `redis:7-alpine` image
- Acts as a caching layer (future-ready)
- Improves scalability and performance

---

## ⚙️ Resource Limits (Noisy Neighbor Prevention)

To prevent any container from exhausting host resources, CPU and memory limits are configured.

| Service | CPU Limit | Memory Limit |
|------|-----------|-------------|
| API | 0.50 CPU | 512 MB |
| PostgreSQL | 0.50 CPU | 512 MB |
| Redis | 0.25 CPU | 256 MB |

### Why This Matters
- Ensures host stability
- Prevents container crashes
- Enables fair resource allocation
- Mimics real production environments

---

## 🚀 How to Build and Run the Application

### 🔧 Prerequisites
- Docker Desktop
- Docker Compose
- Linux containers enabled in Docker Desktop

---

### ▶️ Start the Entire Stack (One Command)

```bash
docker-compose up --build
```
# This command:

- Builds the API Docker image

- Pulls PostgreSQL and Redis images

- Creates Docker network and volumes

- Starts all services in correct order

# 🌐 Application Access
```bash
| Feature          | URL                                                                      |
| ---------------- | ------------------------------------------------------------------------ |
| API Health Check | [http://localhost:8000/](http://localhost:8000/)                         |
| Swagger UI       | [http://localhost:8000/docs](http://localhost:8000/docs)                 |
| OpenAPI JSON     | [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) |
```
# 🧪 Sample API Usage
- Create Traffic Record

Endpoint: POST /traffic
```bash
{
  "location": "Ring Road Jaipur",
  "vehicle_count": 85,
  "avg_speed": 32.5
}
```

- Response
```bash
{
  "message": "Traffic data added successfully",
  "congestion_level": "Medium"
}
```
# 🧠 Data Persistence

- PostgreSQL data is stored in a Docker-managed volume

- Data persists across container restarts

- Containers can be destroyed and recreated safely

# 🛑 Stop the Application
```bash
docker-compose down
```
# Stop and Remove Volumes (Optional)
```bash
docker-compose down -v
```

# 🧪 Validation Steps

- Start containers using Docker Compose

- Verify logs show services running

- Access Swagger UI

- Insert traffic data using POST endpoint

- Confirm data persistence in PostgreSQL container
