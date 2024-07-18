from transactions_ml import transactions_model
from config import conn_params
import psycopg2

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

count = 0
results = transactions_model()
for res in results:
    count += 1
    pred = str(res).split()[1][0:-2]
    cursor.execute("""
                INSERT INTO prediction (prediction)
                VALUES (%s)
            """, (pred,))
    print('Выполнено:', f'{count}/{len(results)}')
    conn.commit()
conn.commit()

# password3000uLtra!

