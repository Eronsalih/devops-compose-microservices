# DevOps Compose Microservices

Simple microservices project built for Docker Compose practice.

## Architecture

React Frontend
      |
      v
FastAPI API Gateway
      |
      +--> Users Service
      |
      +--> Tasks Service

## Technologies

- React
- Vite
- FastAPI
- Python
- Docker
- Docker Compose
- Nginx

## Services

Frontend:
- Host port: 3000
- Container port: 80

API Gateway:
- Host port: 8000
- Container port: 8000

Users Service:
- Host port: 8001
- Container port: 8000

Tasks Service:
- Host port: 8002
- Container port: 8000

## Run Project

Build and start all containers:

docker compose up --build -d

Check containers:

docker compose ps

Stop containers:

docker compose down

## URLs

Frontend:
http://localhost:3000

API Gateway:
http://localhost:8000

Users Service:
http://localhost:8001

Tasks Service:
http://localhost:8002

## API Routes

GET /api/users
POST /api/users

GET /api/tasks
POST /api/tasks

## Docker Structure

The project contains four Dockerfiles:

- Frontend Dockerfile
- API Gateway Dockerfile
- Users Service Dockerfile
- Tasks Service Dockerfile

All services are managed with one docker-compose.yml file.
