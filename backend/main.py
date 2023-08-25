from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from util import get_next_answer
from pydantic import BaseModel

class Message(BaseModel):
    msg: str
origins = [
    "*"
]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def get_answer(message: Message):
    inp = message.msg
    answer = get_next_answer(inp)
    return answer
