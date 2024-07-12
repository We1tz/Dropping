from config import conn_params
import psycopg2
from get_agressive_transactions import get_transaction_agressive

conn = psycopg2.connect(**conn_params)
cursor = conn.cursor()


def top_agressive_users():
    agr_users = []
    agressive_transactions_id = get_transaction_agressive()
    for id_transaction in agressive_transactions_id:
        cursor.execute("SELECT * FROM transactions WHERE id = %s", (id_transaction,))
        information_about_user = cursor.fetchone()
        agr_users.append(information_about_user)

    for i in range(len(agr_users)):
        transaction_id = agr_users[i][0]
        date_transation = agr_users[i][1]
        ammount = agr_users[i][2]
        account_id = agr_users[i][3]
        account_id_out = agr_users[i][4]

        cursor.execute("SELECT * FROM predictions WHERE id = %s", (transaction_id,))
        drop_info = str(float(cursor.fetchone()[1]) * 100) + '%'
        print(
            f'\t Транзакция: {transaction_id} \n время транзации: {date_transation}, \n сумма транзации: {ammount}, \n ID аккаунта с которого совершена транзакция: {account_id}, \n ID куда отправлено {account_id_out}, вероятность дропа: {drop_info} \n')


def get_information_about_profile(account_id):
    cursor.execute("SELECT * FROM transactions WHERE id_acc_in = %s", (account_id,))
    result = cursor.fetchall()




    summ_transfer = 0  # вывод в результат, после присваивания
    transfers = []
    transfers_dates = []

    for i in range(len(result)):  # общий расход пользователя
        summ_transfer += int(result[i][2])
        cursor.execute("SELECT * FROM predictions WHERE id = %s", (result[i][0],))
        danger = cursor.fetchone()[1]

        transfers.append({"date": result[i][1],
                          "ammount": result[i][2],
                          "out_account": result[i][-1],
                          "danger": danger
        })

    print('Переводы пользователя: \n', transfers)
    print('Общий расход:', summ_transfer)

top_agressive_users()
get_information_about_profile("2f1f34d3d9d891f6c6c7b9a3be39ac6d1f0955f900ab9b1f35ba98c1cbf10d8d")
