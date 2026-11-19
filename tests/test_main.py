
import pytest
from fastapi.testclient import TestClient
from app.main import app, tasks
import app.main as main_module

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear()
    main_module.task_counter = 1


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "Python Task Manager"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Check server health",
            "description": "Monitor application",
            "status": "Pending"
        }
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_get_all_tasks():
    client.post(
        "/tasks",
        json={"title": "Deploy application"}
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_task_by_id():
    client.post(
        "/tasks",
        json={"title": "Check AWS services"}
    )

    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Check AWS services"


def test_update_task():
    client.post(
        "/tasks",
        json={"title": "Old task"}
    )

    response = client.put(
        "/tasks/1",
        json={
            "title": "Updated task",
            "description": "Updated description",
            "status": "Completed"
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Completed"


def test_delete_task():
    client.post(
        "/tasks",
        json={"title": "Task to delete"}
    )

    response = client.delete("/tasks/1")

    assert response.status_code == 200


def test_task_not_found():
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_invalid_task():
    response = client.post(
        "/tasks",
        json={"title": ""}
    )

    assert response.status_code == 422
