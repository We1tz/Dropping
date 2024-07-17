import psycopg2
import pandas as pd
import joblib
from api.config import conn_params
from api.modules.process_data import DataPreprocess


def transactions_model():
    def fetch_data(conn_params):
        with psycopg2.connect(**conn_params) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT date, amt, id_acc_in, id_acc_out FROM transactions")
                rows = cursor.fetchall()
                df = pd.DataFrame(rows, columns=['date', 'amt', 'id_acc_in', 'id_acc_out'])
            return df
#

    data = fetch_data(conn_params)
    preprocessor = DataPreprocess(data)
    preprocessed_data = preprocessor.handle_data()
    model = joblib.load('XGB_transaction_model.pkl')

    predictions = model.predict(preprocessed_data)
    prediction_probabilities = model.predict_proba(preprocessed_data)

    return prediction_probabilities

