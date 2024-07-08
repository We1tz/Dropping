import hashlib
import secrets
import time



def generate_token(username):
    current_time = int(time.time() * 1000)
    random_number = secrets.randbits(64)
    data = f'{username}'
    token = hashlib.sha256(data.encode()).hexdigest()

    return token

