from fastapi import FastAPI
from dotenv.main import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
from src.services.todo_service import TodoService
from src.routes.api import router
import os

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(router)
