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

        return {
            "id": transaction_id,
            "date": date_transation,
            "ammount": ammount,
            "account_id": account_id,
            "account_out": account_id_out
        }


def get_information_about_profile_spend(account_id):
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

    summ_danger = 0
    count = 0

    for d in transfers:
        count += 1
        summ_danger += float(d['danger'])

    sred_danger = float(summ_danger / count)

    return {'transfers': transfers,
            'all_sum_transfers': summ_transfer,
            'sred_danger': sred_danger
            }


def get_information_about_profile(account_id):
    # переводы пользователю
    cursor.execute("SELECT * FROM transactions WHERE id_acc_out = %s", (account_id,))
    result = cursor.fetchall()
    transfers = []
    summ_refill = 0

    for n in range(len(result)):
        id_transaction = result[n][0]
        date_transaction = result[n][1]
        ammount = int(result[n][2])
        out_acc = result[n][3]

        cursor.execute("SELECT * FROM predictions WHERE id = %s", (id_transaction,))
        danger = cursor.fetchone()[1]

        transfers.append({"date": date_transaction,
                          "ammount": ammount,
                          "out_account": out_acc,
                          "danger": danger
                          })

        summ_refill += ammount

    return {'transfers': transfers,
            'all_sum_transfers': summ_refill
            }


print(get_information_about_profile_spend('6955aaef36d8bc7d451bc97a03b4897de761c878365510357d8f0ca6d06e62e9'))