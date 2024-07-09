import pandas as pd
import numpy as np

def insert_dataset(data, sep):
    return pd.read_csv(data, sep=sep)

def change_dtypes(df):
    df['flag'] = df['flag'].replace('drop' , 1).fillna(0)
    df['amt'] = df['amt'].apply(lambda x: x.replace(',', '.')).astype('float64')
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y %H:%M')

def create_time_features(df):
    id_in = df['id_acc_in'].unique()
    in_date = []
    for i in id_in: 
        in_date.append(df[df['id_acc_in'] == i]['date'].astype('object').tolist())

    for i in range(len(in_date)):
        for j in range(len(in_date[i])):
            in_date[i][j] = round(in_date[i][j].day * 2.4 + in_date[i][j].hour * 0.1 + in_date[i][j].minute / 600, 2)
    
    for i in range(len(in_date)):
        for j in range(1, len(in_date[i])):
            in_date[i][j] = round(in_date[i][j] - in_date[i][j-1], 2)
        in_date[i][0] = 0

    date_index = []
    for i in range(len(id_in)):
        a = df[df['id_acc_in'] == id_in[i]].index
        date_index.append(a.values.tolist())

    di_w = []
    id_w = []
    for d in date_index:
        for j in d:
            di_w.append(j)
    for i in in_date:
        for j in i:
            id_w.append(j)

    tslt = ["NaN" for i in range(len(df))]
    for i, d in zip(di_w, id_w):
        tslt[i] = d
    df.insert(4, 'time_since_last_tranc', tslt)

    mean_date = in_date
    for i in range(len(mean_date)):
        m = round(np.array(mean_date[i]).mean(), 2)
        for j in range(len(mean_date[i])):
            mean_date[i][j] = m

    md_w = []
    for i in mean_date:
        for j in i:
            md_w.append(j)

    mti = ["NaN" for i in range(len(df))]
    for i, d in zip(di_w, md_w):
        mti[i] = d
    df.insert(5, 'mean_time_interval', mti)

def generate_new_features(df):
    agg_features_in = df.groupby('id_acc_in')['amt'].agg(
        sum_amt_in = 'sum',
        mean_amt_in = 'mean',
        count_amt_in = 'count',
        median_amt_in = 'median'
        
    ).reset_index()

    agg_features_out = df.groupby('id_acc_out')['amt'].agg(
        sum_amt_out = 'sum',
        mean_amt_out = 'mean',
        count_amt_out = 'count',
        median_amt_out = 'median'
    ).reset_index()

    dtf = df.merge(agg_features_in, on='id_acc_in', how='left')
    dtf = dtf.merge(agg_features_out, on='id_acc_out', how='left')
    dtf.fillna(0.0)
    return dtf


def handle_data(data, sep):
    df = insert_dataset(data=data, sep=sep)
    change_dtypes(df)
    create_time_features(df)
    dtf = generate_new_features(df)
    FEATURES = dtf[[x for x in dtf if x != "date" and x != "id_acc_in" and x != "id_acc_out" and x != "flag"]].keys().tolist()
    return dtf[FEATURES]
