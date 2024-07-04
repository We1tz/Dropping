import psycopg2

conn = psycopg2.connect(dbname="users", user="postgres", password="123456", host="192.168.95.14")


def add_user(data):
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s", (data[0],))
    if cursor.fetchone()[0] > 0:
        cursor.close()
        conn.close()
        return 431
    else:
        cursor.execute(
            "INSERT INTO userssite (login, password, telegram, points, attempts, roles, last_login) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            data)
        conn.commit()
        cursor.close()
        conn.close()
        return 200


def check_user(data):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM userssite WHERE login = %s AND password = %s", (data[0], data[1]))
        return 200
    except Exception as e:
        if e:
            print(e)
            return 431



