# Redis connection

ALL_HOST = '193.187.96.199'

REDIS_HOST = f"{ALL_HOST}"
REDIS_PORT = 6379
REDIS_PASSWORD = 'rk8zD5B%wxUYVdsW2&E'

# FASTAPI
secret_key = 'HDle9hWuMPkmcBFbvUmLeszI7ewc7yBSUC-SmxuRbpU'
ALGORITHM = "HS256"
allow_origin = 'http://localhost:3000'

MAX_FAILED_ATTEMPTS = 5
BLOCK_TIME_SECONDS = 10  # 10 sec

conn_params = {
    'dbname': 'main',
    'user': 'we1tz',
    'password': 'awU4NjJeq',
    'host': f'{ALL_HOST}',
    'port': '5432'
}

DB_NAME = conn_params['dbname']
DB_USER = conn_params['user']
DB_PASSWORD = conn_params['password']
DB_HOST = conn_params['host']
DB_PORT = conn_params['port']

smtp_server = 'smtp.antidropping.ru'
smtp_port = 587
smtp_username = 'admin2281337@antidropping.ru'
smtp_password = 'r$U3q#V7&fW3x%'
from_email = 'admin2281337@antidropping.ru'
