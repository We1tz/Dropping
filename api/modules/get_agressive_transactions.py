from api.config import conn_params
import psycopg2
import random

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

#
def get_transaction_agressive():
    cursor.execute("""
        SELECT * FROM predictions
        WHERE to_number(prediction, '9999999D9999999') > 0.54;
    """)

    agressive_users = []
    result = cursor.fetchall()

    for row in result:
        agressive_users.append(row[0])

    transactions_agressive = random.choices(agressive_users, k=7)
    return transactions_agressive

