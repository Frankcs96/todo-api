from fastapi.testclient import TestClient
from src.models.todo import Todo
from src.main import app
from src.services.todo_service import TodoService

client = TestClient(app)


class literal:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


todos_fixture = [
    literal(title="this is title 1", message="hello world", is_done=True,
            created_at="2022-02-25T07:59:07.584Z", updated_at="2022-02-25T07:59:07.584Z"),
    literal(title="this is title 2", message="hello people", is_done=True,
            created_at="2022-02-25T07:59:07.584Z", updated_at="2022-02-25T07:59:07.584Z"),
    literal(title="this is title 3", message="goodbye world", is_done=False,
            created_at="2022-02-25T07:59:07.584Z", updated_at="2022-02-25T07:59:07.584Z"),
    literal(title="this is title 4", message="this is test", is_done=True,
            created_at="2022-02-25T07:59:07.584Z", updated_at="2022-02-25T07:59:07.584Z"),
    literal(title="this is title 5", message="th", is_done=False,
            created_at="2022-02-25T07:59:07.584Z", updated_at="2022-02-25T07:59:07.584Z"),
]


def test_is_done_filter():
    todo_service = TodoService()
    filter_todos = todo_service.filter_by_status(True, todos_fixture)
    assert len(filter_todos) == 3
    filter_todos = todo_service.filter_by_status(False, todos_fixture)
    print(filter_todos)
    assert len(filter_todos) == 2


def test_contains_message_filter():
    todo_service = TodoService()
    filter_todos = todo_service.filter_by_message('world', todos_fixture)
    assert len(filter_todos) == 2
    filter_todos = todo_service.filter_by_message('th', todos_fixture)
    assert len(filter_todos) == 2
    filter_todos = todo_service.filter_by_message('is', todos_fixture)
    assert len(filter_todos) == 1
    filter_todos = todo_service.filter_by_message('ye', todos_fixture)
    assert len(filter_todos) == 1
