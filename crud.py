from fastapi import FastAPI

app = FastAPI()


messages_db = {"0":"first post in FastAPI"}

@app.get("/")
async def get_message(message_id: str) -> str:
    pass

@app.post("/message")
async def