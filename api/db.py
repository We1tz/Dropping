import psycopg2
import bcrypt
from rating import get_rating
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

conn = psycopg2.connect(dbname=f"{DB_NAME}", user=f"{DB_USER}", password=f"{DB_PASSWORD}", host=f"{DB_HOST}")


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def add_user(data):
    login = data[0]
    password = hash_password(data[1])
    email = data[2]
    telegram = data[3]
    rating = data[4]
    role = data[5]
    last_login = data[6]

    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (data[0],))
        if cursor.fetchone()[0] > 0:
            conn.commit()
            return 433
        else:

            cursor.execute(
                "INSERT INTO userssite (login, password, telegram, rating, roles, last_login, email) VALUES (%s, %s, "
                "%s, %s, %s, %s, %s)",
                (login, password, telegram, rating, role, last_login, email))
            conn.commit()
            return 200


def check_user(data):

    password = data[1]
    username = data[0]

    with conn.cursor() as cursor:
        cursor.execute("SELECT password FROM userssite WHERE login = %s", (username,))
        result = cursor.fetchone()
        conn.commit()
        if verify_password(password, result[0]):
            return 200
        else:
            return 431




def update_score(username, score, time):
    with conn.cursor() as cursor:
        rating = get_rating(score, time)
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (username,))
        if cursor.fetchone()[0] > 0:
            cursor.execute(
                "UPDATE userssite SET rating = %s WHERE login = %s",
                (rating, username)
            )
            conn.commit()
            return {
                "result": 200,
                "rating": rating
            }
        else:
            return 404


def get_users_scores():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT login, rating FROM userssite ORDER BY rating DESC")
            results = cursor.fetchall()
            users_scores = [{"username": row[0], "score": row[1]} for row in results]
            conn.commit()
            return users_scores
    except Exception as e:
        print(f"Error: {e}")
        return []


def restore_password(data):

    email = data[0]
    password = data[1]

    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE email = %s", (email,))
        if cursor.fetchone()[0] > 0:
            cursor.execute(
                "UPDATE userssite SET password = %s WHERE login = %s",
                (password, email)
            )
            conn.commit()
            return 200
        else:
            return 404