import random
import string


symbols = '!@#$%^&'
numbers = '0123456789'

def generate_pin():
    code = ''.join(random.choice(numbers) for _ in range(4))
    return code


def generate_password():
    characters = string.ascii_letters + string.digits
    passw = ''.join(random.choice(characters) for _ in range(8))
    password = str(passw) + random.choice(symbols) + random.choice(numbers)
    return password

