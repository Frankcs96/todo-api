from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class PostTodoSchema(BaseModel):
    title: str
    message: str

    class Config:
        orm_mode = True


class TodoSchema(BaseModel):
    id: int
    title: str
    message: str
    is_done: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class PatchStatusTodoSchema(BaseModel):
    is_done: bool

    class Config:
        orm_mode = True
