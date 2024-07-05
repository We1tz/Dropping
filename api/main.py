from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import check_user, add_user
from bot.get_current_date import get_date

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserCredentials(BaseModel):
    username: str
    password: str


@app.post("/login")
async def receive_data(user_credentials: UserCredentials):
    print(user_credentials.username)
    return {"result": check_user((user_credentials.username, user_credentials.password))}


@app.post("/register")
async def register(user_credentials: UserCredentials):
    data = (user_credentials.username, user_credentials.password, 'NaN', 0, 0, 'user', get_date())
    print(user_credentials)
    return {"result": add_user(data)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
