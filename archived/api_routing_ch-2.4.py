from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello world"}

@app.get("/hello/")
async def welcome_user() -> dict:
    return {"message": 'hello, random user'}
#http://127.0.0.1:8000/user?username=vladimir&age=30
@app.get("/user/{user}")
async def welcome_user(username: str, age:int | None = None) -> dict:
    return {"username" :username, "age": age}

@app.get("/user/{user}/{order_id}")
async def welcome_user(order_id: int, user:str) -> dict:
    return {"user": f'hello {user}, this is your order number: {order_id}'}
#http://127.0.0.1:8000/employee/vovan/company/testing_site?department=1
@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {"Employee": name, "Company": company, "Department": department}
#task 1 2.4 chapter
@app.get("/product/{id}")
async def detail_view(id:int | None = None) -> dict:
    return {"product" : f'Stock number {id}'}
#task 2 http://127.0.0.1:8000/users/vladimir/30 == {"user_name":"vladimir","user_age":"30"}
@app.get("/users/{user_name}/{user_age}")
async def users(user_name:str, user_age:int) -> dict:
    return {"user_name": f'{user_name}',"user_age": f'{user_age}'}
#task 3
@app.get("/users/admin")
async def admin_user() -> dict:
    return {"admin_user":'hello administrator'}

@app.get("/users/{user_name}")
async def users(user_name:str) -> dict:
    return {"user_name": f'{user_name}'}

@app.get("/product")
async def product(id:int | None = None):
    return {"id" : f'stock number {id}'}

@app.get("/users")
async def users(name:str, age:int):
    return {"name":f"{name}", "age":f'{id}'}

@app.get("/users_default_age")
async def users(name:str='undefined', age:int=18):
    return {"name":f"{name}", "id":f'{age}'}

country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
}

# Словарь берётся из кода вне декоратора.
# Словарь имеет структуру - Ключ:Значение, поэтому обращаясь к нему как country_dict[country] - мы вытягиваем значения по ключу, то есть написав USA - вытащим
# весь список по ключу, и с помощью [:limit] сможем вывести не все значения, а только часть.
# В случае запроса по пути - переменныая должна совпадать с значением словаря.
@app.get("/country/{country}")
async def list_cities(country: str, limit: int = 2) -> dict:
    return {"country": country, "cities": country_dict[country][:limit]}