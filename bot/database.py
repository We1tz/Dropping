# port 5432

import psycopg2


def add_user(date):
    conn = psycopg2.connect(dbname="base", user="postgres", password="root", host="127.0.0.1")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_id, user_name, date_current, result_current, count_tests) VALUES (%s, %s, %s, %s, %s)",
        date)
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