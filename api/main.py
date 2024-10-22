import datetime
import logging
import os

import jwt
import redis
from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field, validator

from modules.hash import hash_password
from api.config import secret_key, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, BLOCK_TIME_SECONDS, log_formatter, \
    console_handler, log_handler, \
    ALGORITHM, allow_origin
from api.modules.db import check_user, add_user, update_score, get_users_scores, restore_password, \
    update_email_valid, check_true_email_verif, send_pin
from api.modules.generator import generate_password, generate_pin
from api.modules.get_current_date import get_date
from api.modules.mail_send import send_code_mail, send_register_mail, send_password_mail
from api.modules.user_profile import top_agressive_users, get_information_about_profile, \
    get_information_about_profile_spend

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


class UserCredentialsRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)
    email: str

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


class UserCredentialsLogin(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)


class TestResults(BaseModel):
    res: int
    type: int


class Restore(BaseModel):
    email: str
    code: str


class PostCode(BaseModel):
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


def generate_confirmation_url(email: str):
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24)
    payload = {"sub": email, "exp": expiration}
    confirmation_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    confirmation_url = f"http://antidropping.ru/api/confirm?token={confirmation_token}"
    return confirmation_url


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
async def receive_data(user_credentials: UserCredentialsLogin, response: Response):
    data = (user_credentials.username, user_credentials.password)
    status = check_user(data=data)
    if status == 200:
        reset_failed_attempts(user_credentials.username)
        access_token = create_access_token({"sub": user_credentials.username})
        refresh_token = create_refresh_token({"sub": user_credentials.username})
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        return {
            "result": True,
            "access_token": access_token
        }
    else:
        if status == 201:
            reset_failed_attempts(user_credentials.username)
            return {'information:' 'valid your mail'}
        else:
            record_failed_attempt(user_credentials.username)
            return {"result": 431}


@app.post("/register")
async def register(user_credentials: UserCredentialsRegister):
    try:
        hashed_password = hash_password(user_credentials.password)
        email = user_credentials.email
        data = (user_credentials.username, hashed_password, email, 'None', 0, 'user', get_date(), 'False')
        status = add_user(data)
        if status == 200:
            send_register_mail((email, generate_confirmation_url(user_credentials.username)))
        else:
            return 431
    except Exception as e:
        app_logger.error(f"Error during registration: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/confirm")
async def confirm_registration(token: str, response: Response, ):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=400, detail="Invalid token")
        if username:
            if update_email_valid(username) == 200:
                access_token = create_access_token({"sub": username})
                refresh_token = create_refresh_token({"sub": username})
                response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
                return RedirectResponse(url="redirect", status_code=301)
            else:
                return Exception
        else:
            raise HTTPException(status_code=400, detail="Ошибка подтверждения регистрации")
    except Exception as e:
        app_logger.error(f"Error during confirmation: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/refresh")
async def protected_route(request: Request):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Токен не найден")
    return {"message": "Вы уже авторизованы", "user": verify_token(refresh_token)["sub"]}


@app.post("/approve")
async def approve(reset: PostCode):
    email = reset.email
    code = generate_pin()
    if send_pin((email, code)) == 200:
        send_code_mail((email, code))
        return 200
    else:
        return 404


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
    code = restore.code
    email = restore.email
    new_password = generate_password()
    status = restore_password((email, new_password, code))
    if status == 200:
        send_password_mail((email, new_password))
        return RedirectResponse(url="redirect", status_code=301)
    else:
        return 431


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
