from fastapi import FastAPI, Response, Request, HTTPException, Depends
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

SECRET_KEY = "HDle9hWuMPkmcBFbvUmLeszI7ewc7yBSUC-SmxuRbpU"  
ALGORITHM = "HS256"


class UserCredentials(BaseModel):
    username: str
    password: str


def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/login")
async def receive_data(user_credentials: UserCredentials, response: Response):
    result = check_user((user_credentials.username, user_credentials.password))
    if result:
        access_token = create_access_token({"sub": user_credentials.username})
        refresh_token = create_refresh_token({"sub": user_credentials.username})
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        return {
            "result": result,
            "access_token": access_token
        }
    else:
        return {"result": result}


@app.post("/register")
async def register(user_credentials: UserCredentials, response: Response):
    data = (user_credentials.username, user_credentials.password, 'NaN', 0, 0, 'user', get_date())
    print(user_credentials)
    add_result = add_user(data)

    print(add_result)

    if add_result == 200:
        access_token = create_access_token({"sub": user_credentials.username})
        refresh_token = create_refresh_token({"sub": user_credentials.username})
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        return {
            "result": add_result,
            "access_token": access_token
        }
    else:
        return {"result": add_result}#


@app.get("/refresh")
async def protected_route(request: Request):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Токен не найден")
    payload = verify_token(refresh_token)
    return {"message": "Вы уже авторизованы", "user": payload["sub"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
