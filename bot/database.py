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
    print('Данные добавлены')
