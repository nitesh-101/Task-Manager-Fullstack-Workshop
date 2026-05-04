# tests/test_app.py

import json
import pytest
from app import app, tasks, next_id


@pytest.fixture
def client():
    """Create a test client and reset in-memory database before each test."""
    app.config['TESTING'] = True

    with app.test_client() as client:
        # Reset state
        global tasks, next_id
        tasks.clear()

        # Reset next_id to 1
        import app as app_module
        app_module.tasks = []
        app_module.next_id = 1

        yield client


def test_get_tasks_empty(client):
    resp = client.get('/tasks')
    assert resp.status_code == 200
    assert json.loads(resp.data) == []


def test_create_task_success(client):
    resp = client.post('/tasks', json={"title": "Test task"})
    assert resp.status_code == 201

    data = json.loads(resp.data)
    assert data['title'] == "Test task"
    assert data['done'] is False
    assert 'id' in data


def test_create_task_invalid(client):
    resp = client.post('/tasks', json={"title": ""})
    assert resp.status_code == 400
    assert "Title cannot be empty" in json.loads(resp.data)['error']


def test_create_task_requires_json(client):
    resp = client.post('/tasks', data="not json", content_type='text/plain')
    assert resp.status_code == 400


def test_get_task_by_id(client):
    # First create a task
    client.post('/tasks', json={"title": "Sample"})

    resp = client.get('/tasks/1')
    assert resp.status_code == 200

    data = json.loads(resp.data)
    assert data['id'] == 1


def test_get_task_not_found(client):
    resp = client.get('/tasks/999')
    assert resp.status_code == 404


def test_update_task(client):
    client.post('/tasks', json={"title": "Old"})

    resp = client.put('/tasks/1', json={"title": "New", "done": True})
    assert resp.status_code == 200

    data = json.loads(resp.data)
    assert data['title'] == "New"
    assert data['done'] is True


def test_delete_task(client):
    client.post('/tasks', json={"title": "Delete me"})

    resp = client.delete('/tasks/1')
    assert resp.status_code == 200

    # Ensure it's deleted
    resp = client.get('/tasks/1')
    assert resp.status_code == 404