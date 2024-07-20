import pandas as pd


def mean_drop_features(df: pd.DataFrame, target_column_name='flag', date_column_name='date'):
    df = df[df[target_column_name] == 1].describe()
    mean_values = df.loc['mean'].tolist()
    mean_names = df.loc['mean'].index.tolist()
    d = dict(zip(mean_names, mean_values))
    d.pop(date_column_name)
    d.pop(target_column_name)
    return d