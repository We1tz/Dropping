from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import check_user, add_user
from bot.get_current_date import get_date
import jwt
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "2b5c2317ed40ea98188df590e14be0ac5935785f5e3f01b8721ad6b7f75e5f65"  # Используйте постоянный секретный ключ
ALGORITHM = "HS256"


class UserCredentials(BaseModel):
    username: str
    password: str


def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/login")
async def receive_data(user_credentials: UserCredentials):
    print(user_credentials.username)
    return {"result": check_user((user_credentials.username, user_credentials.password))}


@app.post("/register")
async def register(user_credentials: UserCredentials):
    data = (user_credentials.username, user_credentials.password, 'NaN', 0, 0, 'user', get_date())
    print(user_credentials)
    add_result = add_user(data)

    if add_result == 200:
        access_token = create_access_token({"sub": user_credentials.username})
        refresh_token = create_refresh_token({"sub": user_credentials.username})
        return {
            "result": add_result,
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    else:
        return {"result": add_result}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
