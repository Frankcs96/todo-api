
from src.models.todo import Todo


class TodoService():

    def filter_by_status(self, is_done_filter: bool, todos: list[Todo]):
        filter_todos_by_status = []
        for todo in todos:
            if todo.is_done and is_done_filter:
                filter_todos_by_status.append(todo)
            if todo.is_done == False and is_done_filter == False:
                filter_todos_by_status.append(todo)

        return filter_todos_by_status

    def filter_by_message(self, contains_text_filter: str, todos: list[Todo]):
        filter_todos_by_message = []
        for todo in todos:
            if todo.message.find(contains_text_filter) != -1:
                filter_todos_by_message.append(todo)

        return filter_todos_by_message
