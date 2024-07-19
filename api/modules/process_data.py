import pandas as pd
import numpy as np

class DataPreprocess:
    def __init__(self, data):
        self.data = data

    def change_dtypes(self):
        self.data['amt'] = self.data['amt'].apply(lambda x: x.replace(',', '.')).astype('float64')
        self.data['date'] = pd.to_datetime(self.data['date'], format='%d.%m.%Y %H:%M')

    def create_time_features(self):
        id_in = self.data['id_acc_in'].unique()
        in_date = []
        for i in id_in: 
            in_date.append(self.data[self.data['id_acc_in'] == i]['date'].astype('object').tolist())

        for i in range(len(in_date)):
            for j in range(len(in_date[i])):
                in_date[i][j] = round(in_date[i][j].day * 2.4 + in_date[i][j].hour * 0.1 + in_date[i][j].minute / 600, 2)
        
        for i in range(len(in_date)):
            for j in range(1, len(in_date[i])):
                in_date[i][j] = round(in_date[i][j] - in_date[i][j-1], 2)
            in_date[i][0] = 0

        date_index = []
        for i in range(len(id_in)):
            a = self.data[self.data['id_acc_in'] == id_in[i]].index
            date_index.append(a.values.tolist())

        di_w = []
        id_w = []
        for d in date_index:
            for j in d:
                di_w.append(j)
        for i in in_date:
            for j in i:
                id_w.append(j)

        tslt = ["NaN" for i in range(len(self.data))]
        for i, d in zip(di_w, id_w):
            tslt[i] = d
        self.data.insert(4, 'time_since_last_tranc', tslt)

        mean_date = in_date
        for i in range(len(mean_date)):
            m = round(np.array(mean_date[i]).mean(), 2)
            for j in range(len(mean_date[i])):
                mean_date[i][j] = m

        md_w = []
        for i in mean_date:
            for j in i:
                md_w.append(j)

        mti = ["NaN" for i in range(len(self.data))]
        for i, d in zip(di_w, md_w):
            mti[i] = d
        self.data.insert(5, 'mean_time_interval', mti)

    def generate_new_features(self):
        agg_features_in = self.data.groupby('id_acc_in')['amt'].agg(
            sum_amt_in = 'sum',
            mean_amt_in = 'mean',
            count_amt_in = 'count',
            median_amt_in = 'median'
            
        ).reset_index()

        agg_features_out = self.data.groupby('id_acc_out')['amt'].agg(
            sum_amt_out = 'sum',
            mean_amt_out = 'mean',
            count_amt_out = 'count',
            median_amt_out = 'median'
        ).reset_index()

        dtf = self.data.merge(agg_features_in, on='id_acc_in', how='left')
        dtf = dtf.merge(agg_features_out, on='id_acc_out', how='left')
        dtf.fillna(0.0)
        return dtf


    def handle_data(self):
        self.change_dtypes()
        self.create_time_features()
        dtf = self.generate_new_features()
        FEATURES = dtf[[x for x in dtf if x != "date" and x != "id_acc_in" and x != "id_acc_out" and x != "flag"]].keys().tolist()
        return dtf[FEATURES]
