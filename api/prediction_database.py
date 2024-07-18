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
<<<<<<< HEAD
                INSERT INTO prediction (prediction)
                VALUES (%s)
            """, (pred,))
=======
                INSERT INTO prediction (id, predict)
                VALUES (%s, %s)
            """, (count, pred,))
>>>>>>> 4367864bd1064d94b9d8b3f5ae650eaf8b8c4775
    print('Выполнено:', f'{count}/{len(results)}')
    conn.commit()
conn.commit()



