from typing import Annotated
from fastapi import FastAPI, Path, Query
#_path_query_ch-2.5
app = FastAPI()

# Использование PATH

# Стандартный пример применения path
# @app.get("/user/{username}/{age}")
# async def login(username: str = Path(min_length=3, max_length=15, description='Enter your username', example='Vladimir'),
#                 age: int = Path(ge=0, le=100, description="enter your age")) -> dict:
#     return {"user": username, "age": age}

# Просто поменяли то что не юзает path в начало, т.к. синтаксис так устроен
# @app.get("/user/{username}/{age}")
# async def login(age: int, username: str = Path(min_length=3, max_length=15, description='Enter your username', example='Vladimir')) -> dict:
#     return {"user": username, "age": age}

# Вариант с annotated
# @app.get("/user/{username}/{age}")
# async def login(
#         username: Annotated[str, Path(min_length=3, max_length=15, description='Enter your username', example='Vladimir')],
#         age: int) -> dict:
#     return {"user": username, "age": age}

# Использование QUERY

