from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Users Service", version="1.0.0")


class UserCreate(BaseModel):
    name: str
    email: str


users = [
    {
        "id": 1,
        "name": "Eron",
        "email": "eron@example.com"
    }
]


@app.get("/")
def root():
    return {
        "service": "users-service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.post("/users")
def create_user(user: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)
    return new_user
