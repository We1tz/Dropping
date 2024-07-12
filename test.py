import psycopg2
from api.config import conn_params


conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()
cursor.execute("""SELECT * FROM predictions""")
result = cursor.fetchall()
data = []

for res in result:
    nu = float(res[1])
    data.append(nu)

print(min(data))