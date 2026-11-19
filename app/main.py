
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, Literal

app = FastAPI(
    title="Python Task Manager API",
    description="A Task Manager application for AWS DevOps learning",
    version="1.0.0"
)

# Request data validation
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: Optional[str] = None
    status: Literal["Pending", "In Progress", "Completed"] = "Pending"


class TaskResponse(TaskCreate):
    id: int


# Temporary application storage
tasks = {}
task_counter = 1


# 1. Welcome endpoint
@app.get("/")
def home():
    return {
        "application": "Python Task Manager",
        "message": "Welcome to Task Manager API",
        "version": "1.0.0"
    }


# 2. Application health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "task-manager"
    }


# 3. Create a new task
@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):

    global task_counter

    new_task = {
        "id": task_counter,
        **task.model_dump()
    }

    tasks[task_counter] = new_task
    task_counter += 1

    return new_task


# 4. Get all tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks():
    return list(tasks.values())


# 5. Get task by ID
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


# 6. Update existing task
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: TaskCreate):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    tasks[task_id] = {
        "id": task_id,
        **updated_task.model_dump()
    }

    return tasks[task_id]


# 7. Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[task_id]

    return {
        "message": "Task deleted successfully",
        "task_id": task_id
    }
