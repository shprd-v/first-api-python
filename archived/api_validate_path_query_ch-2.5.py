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

# @app.get("/user/{username}")
# async def login(
#         username: Annotated[str, Path(min_length=3, max_length=15, description='Enter your username', example='shprd')],
#         first_name: Annotated[str | None, Query(max_length=10)] = None) -> dict:
#     return {"user": username, "Name": first_name}

# @app.get("/user/{username}")
# async def login(
#         username: Annotated[str, Path(min_length=3, max_length=15, description='Enter your username', example='shprd')],
#         # В Query нельзя использовать default внутри аннотации, это задается простым значением вместо None, Обязательность параметра указывается многоточнием
#         first_name: Annotated[str | None, Query(max_length=10)] = ...) -> dict:
#     return {"user": username, "Name": first_name}

# @app.get("/user/{username}")
# async def login(
#         #Если по каким-то причинам мы хотим использовать Query без Annotated, то следует использовать следующий синтаксис:
#         username: str = Path(min_length=3, max_length=15, description='Enter your username', example='shprd'),
#         # Также с помощью параметра include_in_schema мы можем исключить данный параметр из документации.
#         first_name: str = Query(default=None, max_length=10, include_in_schema=False)) -> dict:
#     return {"user": username, "Name": first_name}

# А вот так через QUERY выводим список по запросу.
@app.get("/user")
async def search(people: Annotated[list[str], Query()]) -> dict:
    return {"user": people}

# Можно и без Annotated
# @app.get("/user")
# async def search(people: List[str] = Query(...)):
#     return {"user": people}

# Или с нативным списком Python:
# @app.get("/user")
# async def search(people: list[str] = Query(...)):
#     return {"user": people}

# Есть ещё regex, используем встроенный моудуль re и вносим как параметр к query: regex="^J|s$"

@app.get("/user/{username}")
async def login(
        username: Annotated[
            str, Path(min_length=3, max_length=15)],
        first_name: Annotated[
            str | None, Query(max_length=100, description='Enter your username. Should starts with "J" and ends with "s"', example='John Stills', regex="^J|s$")] = None) -> dict:
    return {"user": username, "Name": first_name}
# Передана строка john stills что совпадает с регексом и входит по длине.

@app.get("/users/{name}")
async def users(name: str = Path(min_length=4, max_length=20, description="Enter your name")) -> dict:
    return {"user_name": f'{name}'}

@app.get("/category/{category_id}/procudts")
async def category(category_id: int = Path(gt=0,description="description of field category_id: this is a id of category of our products"),
                    page = int) -> dict:
    return {"category id is: ": {category_id}, "Page number is: " : {page}}
