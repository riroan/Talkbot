from fastapi import FastAPI
from util import get_next_answer
from pydantic import BaseModel

class Message(BaseModel):
    msg: str

app = FastAPI()

@app.post("/")
async def get_answer(message: Message):
    inp = message.msg
    answer = get_next_answer(inp)
    return answer
