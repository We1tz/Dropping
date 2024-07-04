from fastapi import FastAPI
from pydantic import BaseModel
from db import add_user, check_user
from backend.date import get_date

app = FastAPI()


class UserCredentials(BaseModel):
    username: str
    password: str

#
@app.post("/login")
async def receive_data(user_credentials: UserCredentials):
    user_name = user_credentials.username
    user_password = user_credentials.password
    res = check_user((user_name, user_password))
    return {"result": res}


@app.post("/register")
async def receive_data(user_credentials: UserCredentials):
    user_name = user_credentials.username
    user_password = user_credentials.password
    res = add_user((user_name, user_password, 'NaN', 0, 0, 'user', get_date()))
    print(res)
    return {"result": res}
