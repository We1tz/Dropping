import psycopg2
import bcrypt

conn = psycopg2.connect(dbname="users", user="postgres", password="123456", host="192.168.95.14")


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def add_user(data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (data[0],))
        if cursor.fetchone()[0] > 0:
            conn.commit()
            return 433
        else:
            hashed_password = hash_password(data[1])
            cursor.execute(
                "INSERT INTO userssite (login, password, telegram, points, attempts, roles, last_login) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (data[0], hashed_password, data[2], data[3], data[4], data[5], data[6]))
            conn.commit()
            return 200


def check_user(username: str):
    with conn.cursor() as cursor:
        cursor.execute("SELECT password FROM userssite WHERE login = %s", (username,))
        result = cursor.fetchone()
        conn.commit()
        if result:
            return {"username": username, "password_hash": result[0]}
        else:
            return 431


def update_score(data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (data[0],))
        if cursor.fetchone()[0] > 0:
            cursor.execute(
                "UPDATE userssite SET points = %s, attempts = %s WHERE login = %s",
                (data[1], data[2], data[0])
            )
            conn.commit()
            return 200
        else:
            return 404
