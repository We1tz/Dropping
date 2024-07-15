from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import check_user, add_user, hash_password, update_score, get_users_scores, restore_password
from get_current_date import get_date
import jwt
import datetime
from generator import generate_password
import redis
from user_profile import top_agressive_users, get_information_about_profile, get_information_about_profile_spend
import os
from mail_send import send_password_mail
import logging
from pydantic import BaseModel, Field, validator
from config import secret_key, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, BLOCK_TIME_SECONDS, log_formatter, \
    console_handler, log_handler, \
    ALGORITHM, allow_origin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"{allow_origin}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = os.getenv("SECRET_KEY", f"{secret_key}")

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=f'{REDIS_PASSWORD}', decode_responses=True)

log_handler.setFormatter(log_formatter)
console_handler.setFormatter(log_formatter)
app_logger = logging.getLogger()
app_logger.setLevel(logging.INFO)
app_logger.addHandler(log_handler)
app_logger.addHandler(console_handler)


class UserCredentials(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)

    @validator("password")
    def password_complexity(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not any(char.isupper() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
        if not any(char.islower() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну строчную букву")
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" for char in value):
            raise ValueError("Пароль должен содержать хотя бы один специальный символ")
        return value


class TestResults(BaseModel):
    res: int
    type: int


class Restore(BaseModel):
    email: str

class TransactionUser(BaseModel):
    identifier: str


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
        raise HTTPException(status_code=401, detail="Срок действия токена истек")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Неверный токен")


def get_failed_attempts_key(username: str) -> str:
    return f"failed_attempts:{username}"


def is_user_blocked(username):
    key = f"failed_attempts:{username}"
    failed_attempts = redis_client.get(key)
    if failed_attempts is None:
        return False
    return int(failed_attempts) >= 3


def record_failed_attempt(username: str):
    key = get_failed_attempts_key(username)
    failed_attempts = redis_client.incr(key)
    if int(failed_attempts) == 1:
        redis_client.expire(key, BLOCK_TIME_SECONDS)


def reset_failed_attempts(username: str):
    key = get_failed_attempts_key(username)
    redis_client.delete(key)


@app.post("/login")
async def receive_data(user_credentials: UserCredentials, response: Response):
    if check_user((user_credentials.username, user_credentials.password)) == 200:
        reset_failed_attempts(user_credentials.username)
        access_token = create_access_token({"sub": user_credentials.username})
        refresh_token = create_refresh_token({"sub": user_credentials.username})
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        return {
            "result": True,
            "access_token": access_token
        }
    else:
        record_failed_attempt(user_credentials.username)
        return {"result": False}


@app.post("/register")
async def register(user_credentials: UserCredentials, response: Response):
    try:
        hashed_password = hash_password(user_credentials.password)
        email = user_credentials.email

        data = (user_credentials.username, hashed_password, email, 'None', 0, 'user', get_date())
        result = add_user(data)

        if result == 200:
            access_token = create_access_token({"sub": user_credentials.username})
            refresh_token = create_refresh_token({"sub": user_credentials.username})
            response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
            return {
                "result": result,
                "username": user_credentials.username,
                "access_token": access_token
            }
        else:
            return {"result": 431}
    except Exception as e:
        app_logger.error(f"Error during registration: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/refresh")
async def protected_route(request: Request):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Токен не найден")
    return {"message": "Вы уже авторизованы", "user": verify_token(refresh_token)["sub"]}


@app.post("/sendvect")
async def send_test_results(request: Request, test_results: TestResults):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Токен не найден")
    payload = verify_token(refresh_token)
    username = payload["sub"]
    score = test_results.res
    time = test_results.type

    return update_score(username, score, time)


@app.post("/restore")
async def restore(response: Response, restore: Restore):
    new_password = generate_password()
    result = restore_password((restore.email, hash_password(new_password)))
    if result == 200:
        send_password_mail((restore.email, new_password))
        response.delete_cookie(key="refresh_token")
        return 'Пароль изменен'
    else:
        return 404


#@app.get("/transactions")
#async def transactions(response: Response):
  #  result = transaction_model()
   # return {'result': 200,
     #       'model': result}


@app.get("/agressiveusers")
async def argessive_users():
    all_result = []
    for i in range(0, 6):
        result = top_agressive_users()
        all_result.append(result)

    return {
            'result': 200,
            'information': all_result
    }

@app.post("/getaboutprofile")
async def get_info_about_profile(transuser: TransactionUser):
    ident = transuser.identifier
    result = get_information_about_profile(ident)
    result2 = get_information_about_profile_spend(ident)

    if not result['transfers']:
        return result2
    else:
        return result

@app.get("/getvect")
async def send_test_results():
    result = get_users_scores()
    return result


@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="refresh_token")
    return {"message": "Успешно"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
