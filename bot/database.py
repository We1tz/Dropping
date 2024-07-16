# port 5432

import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

conn = psycopg2.connect(dbname=f"{DB_NAME}", user=f"{DB_USER}", password=f"{DB_PASSWORD}", host=f"{DB_HOST}")


def add_user(date):

    id = date[0]
    tg = date[1]
    role = date[2]
    register = date[3]

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO userstg (id, telegram, roles, register) VALUES (%s, %s, %s, %s)",(id, tg, role, register))
    conn.commit()
    cursor.close()
    conn.close()


def select_from_base():
    conn = psycopg2.connect(dbname="base", user="postgres", password="root", host="127.0.0.1")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users")
    data_result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data_result