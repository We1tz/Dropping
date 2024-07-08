import psycopg2

conn = psycopg2.connect(dbname="users", user="postgres", password="123456", host="192.168.95.14")


def add_user(data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (data[0],))
        if cursor.fetchone()[0] > 0:
            conn.commit()
            return 431
        else:
            cursor.execute(
                "INSERT INTO userssite (login, password, telegram, points, attempts, roles, last_login) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                data)
            conn.commit()
            return 200


def check_user(data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s AND password = %s", (data[0], data[1]))
        count = cursor.fetchone()[0]
        conn.commit()
        if count > 0:
            return 200
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


print(update_score(('Weitz', 5, 5000)))
