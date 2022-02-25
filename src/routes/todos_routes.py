from operator import is_
from typing import Optional
from fastapi import APIRouter, status
from src.services.todo_service import TodoService
from src.models.todo import Todo
from src.schemas.todo_schema import PatchStatusTodoSchema, TodoSchema, PostTodoSchema
from fastapi_sqlalchemy import db
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/v1/todos",
    tags=["Todos"],
)


@router.get("", response_model=list[TodoSchema])
def get_todos(is_done_filter: Optional[bool] = None, contains_text_filter: Optional[str] = None):
    todos = db.session.query(Todo).all()
    todo_service = TodoService()
    if is_done_filter is not None:
        todos = todo_service.filter_by_status(is_done_filter, todos)

    if contains_text_filter is not None:
        todos = todo_service.filter_by_message(contains_text_filter, todos)
        pass
    return todos


@router.post("", response_model=TodoSchema, status_code=status.HTTP_201_CREATED)
def add_todo(todo: PostTodoSchema):
    todo_to_store = Todo(
        title=todo.title, message=todo.message, is_done=False)
    db.session.add(todo_to_store)
    db.session.commit()

    return todo_to_store


@router.delete("/{id}", responses={404: {}, 200: {}})
def delete_todo(id: int):
    rows_deleted = db.session.query(Todo).filter(Todo.id == id).delete()
    if rows_deleted == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    db.session.commit()


@router.patch("/{id}", response_model=TodoSchema, responses={404: {}, 200: {"model": TodoSchema}})
def change_todo_status(id: int, todo_status: PatchStatusTodoSchema):
    todo_to_patch = db.session.query(Todo).filter(Todo.id == id).first()
    if todo_to_patch is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    todo_to_patch.is_done = todo_status.is_done
    db.session.commit()
    return todo_to_patch
