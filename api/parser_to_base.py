from config import conn_params
import psycopg2

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

vac = 'сюда вакансию'


cursor.execute("""
        INSERT INTO vacancy (text_vac)
        VALUES (%s)
    """, (vac,))


conn.commit()
cursor.close()
conn.close()


