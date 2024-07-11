import pandas as pd
import psycopg2
from config import conn_params

csv_file_path = 'датасет.csv'
df = pd.read_csv(csv_file_path, sep=';')
data_list = df.to_dict(orient='records')

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()

for record in data_list:
    date = record['date']
    amt = record['amt']
    acc_in = record['id_acc_in']
    acc_out = record['id_acc_out']
    cursor.execute("""
        INSERT INTO transactions (date, amt, id_acc_in, id_acc_out)
        VALUES (%s, %s, %s, %s)
    """, (date, amt, acc_in, acc_out))
    print('DONE')
    conn.commit()
conn.commit()
