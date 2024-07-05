import hashlib
import secrets
import time
import random


def generate_token(username):
    current_time = int(time.time() * 1000)
    random_number = secrets.randbits(64)
    data = f'{username}'
    token = hashlib.sha256(data.encode()).hexdigest()

    return token


print(generate_token(random.uniform(2.5, 10.0)))