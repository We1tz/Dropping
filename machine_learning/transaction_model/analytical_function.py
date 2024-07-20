import pandas as pd


def mean_drop_features(df: pd.DataFrame, target_column_name='flag', date_column_name='date'):
    df = df[df[target_column_name] == 1].describe()
    mean_values = df.loc['mean'].tolist()
    mean_names = df.loc['mean'].index.tolist()
    d = dict(zip(mean_names, mean_values))
    d.pop(date_column_name)
    d.pop(target_column_name)
    return d


def above_mean(mean_features_dict: dict[str, float], transation: pd.Series, target_column_name='flag', date_column_name='date',
               ids_columns=['id_acc_out', 'id_acc_in']) -> dict:
    drop_columns_name = ids_columns
    drop_columns_name.append(target_column_name)
    drop_columns_name.append(date_column_name)
    transation = transation.drop(drop_columns_name)
    suspect_matrix = []
    features_name = transation.index.tolist()
    for mean_feature, transation_feature in zip(list(mean_features_dict.values()), transation.tolist()):
        if transation_feature > mean_feature:
            suspect_matrix.append(1)
        else:
            suspect_matrix.append(0)
    return dict(zip(features_name, suspect_matrix))
    