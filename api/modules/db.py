import psycopg2

from api.config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST
from api.modules.hash import verify_password
from api.modules.rating import get_rating
from api.modules.hash import hash_password

conn = psycopg2.connect(dbname=f"{DB_NAME}", user=f"{DB_USER}", password=f"{DB_PASSWORD}", host=f"{DB_HOST}")


def add_user(data):
    login = data[0]
    password = data[1]
    email = data[2]
    telegram = data[3]
    rating = data[4]
    role = data[5]
    last_login = data[6]

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM userssite WHERE login = %s OR email = %s", (data[0], data[2]))
        if cursor.fetchone():
            conn.commit()
            return 433

        else:
            cursor.execute(
                "INSERT INTO userssite (login, password, telegram, rating, roles, last_login, email, emailvalid) VALUES (%s, %s, "
                "%s, %s, %s, %s, %s, %s)",
                (login, password, telegram, rating, role, last_login, email, 'False'))
            conn.commit()
            return 200



def check_user(data):
    password = data[1]
    username = data[0]

    with conn.cursor() as cursor:
        cursor.execute("SELECT password FROM userssite WHERE login=%s", (username,))
        result = cursor.fetchone()
        conn.commit()
        if verify_password(password, result[0]):
            cursor.execute("SELECT emailvalid FROM userssite WHERE login = %s", (username,))
            res = cursor.fetchone()
            if res[0] == 'True':
                return 200
            else:
                return 201
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

    email = str(data[0])
    password = hash_password(str(data[1]))
    code = str(data[2])


    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE email = %s AND last_code = %s", (email, code,))
        if cursor.fetchone()[0] > 0:
            cursor.execute(
                "UPDATE userssite SET password = %s WHERE email = %s",
                (password, email,)
            )
            conn.commit()
            return 200
        else:
            return 404


def update_email_valid(username):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (username,))
        if cursor.fetchone()[0] > 0:
            cursor.execute(
                "UPDATE userssite SET emailvalid = %s WHERE login = %s",
                ('True', username)
            )
            conn.commit()
            return 200
        else:
            return 404


def check_true_email_verif(username):
    with conn.cursor() as cursor:
        cursor.execute("SELECT emailvalid FROM userssite WHERE login = %s", (username,))
        status = cursor.fetchone()
        if status == 'True':
            return 200
        else:
            return 431


def send_pin(data):
    email = data[0]
    code = data[1]
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE email = %s", (email,))
        if cursor.fetchone()[0] > 0:
            cursor.execute(
                "UPDATE userssite SET last_code = %s WHERE email = %s",
                (code, email,)
            )
            conn.commit()
            return 200
        else:
            return 404

