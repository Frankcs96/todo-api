from fastapi.testclient import TestClient
from src.schemas.todo_schema import PostTodoSchema
from src.main import app

client = TestClient(app)

wrong_post_todo_fixtures = {
    "title": "title of todo 1",
    "message": "hello world",
    "is_done": False,
    "created_at": "2022-02-25T07:59:07.584Z",
    "updated_at": "2022-02-25T07:59:07.584Z"
},

post_todo_fixtures: PostTodoSchema = {
    "title": "title of todo 1",
    "message": "hello world"
}

# since this a test exercise Ill test with production db, the ideal solution would be to create a test database for testing.


def test_health_check():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'health': True}


def test_get_all_todos():
    response = client.get('/v1/todos')
    assert response.status_code == 200
    # cannot test return data since I'm using the same production db so I don't know how many
    # todos will be getting.


def test_get_todos_with_filters():
    response = client.get(
        '/v1/todos?is_done_filter=true&contains_text_filter=world')
    assert response.status_code == 200


def test_post_todo():
    response = client.post('/v1/todos', json=post_todo_fixtures)
    assert response.status_code == 201
    assert response.json()['is_done'] == False
    assert response.json()['created_at'] is not None
    response = client.post('/v1/todos', json=wrong_post_todo_fixtures)
    assert response.status_code == 422


def test_delete_todo():
    todo_id_to_delete = client.post(
        '/v1/todos', json=post_todo_fixtures).json()['id']
    response = client.delete(f'/v1/todos/{todo_id_to_delete}')
    assert response.status_code == 200
    response = client.delete(f'/v1/todos/-33')
    assert response.status_code == 404


def test_update_todo_status():

    todo_id_to_update = client.post(
        '/v1/todos', json=post_todo_fixtures).json()['id']

    response = client.patch(
        f'/v1/todos/{todo_id_to_update}', json={'is_done': True})

    assert response.status_code == 200
    assert response.json()['is_done'] == True
    assert response.json()['updated_at'] is not None

    response = client.patch(
        f'/v1/todos/-33', json={'is_done': True})
    assert response.status_code == 404
