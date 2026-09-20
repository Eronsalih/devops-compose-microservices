import os

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Gateway",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USERS_SERVICE_URL = os.getenv(
    "USERS_SERVICE_URL",
    "http://localhost:8001"
)

TASKS_SERVICE_URL = os.getenv(
    "TASKS_SERVICE_URL",
    "http://localhost:8002"
)


@app.get("/")
def root():
    return {
        "service": "api-gateway",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# -------------------------
# USERS SERVICE
# -------------------------

@app.get("/api/users")
async def get_users():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{USERS_SERVICE_URL}/users"
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail="Users service unavailable"
        )


@app.post("/api/users")
async def create_user(user: dict):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{USERS_SERVICE_URL}/users",
                json=user
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail="Users service unavailable"
        )


# -------------------------
# TASKS SERVICE
# -------------------------

@app.get("/api/tasks")
async def get_tasks():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TASKS_SERVICE_URL}/tasks"
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail="Tasks service unavailable"
        )


@app.post("/api/tasks")
async def create_task(task: dict):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{TASKS_SERVICE_URL}/tasks",
                json=task
            )

        response.raise_for_status()
        return response.json()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail="Tasks service unavailable"
        )
