from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tasks Service", version="1.0.0")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


tasks = [
    {
        "id": 1,
        "title": "Learn Docker Compose",
        "completed": False
    }
]


@app.get("/")
def root():
    return {
        "service": "tasks-service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    for existing_task in tasks:
        if existing_task["id"] == task_id:
            existing_task["title"] = task.title
            existing_task["completed"] = task.completed
            return existing_task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {
                "message": "Task deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
