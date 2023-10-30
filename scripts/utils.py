import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def data_preparation(PATH):
    df = pd.read_csv(PATH)
    df = df[df["Energie"] != 'electric']

    categorical = list(df.dtypes[df.dtypes == 'object'].index)
    numerical = [i for i in list(df.columns) if i not in categorical]
    numerical.pop(-1)
    for c in numerical:
        df[c] = df[c].fillna(df[c].median())
        
    df["Emission CO2"] = df["Emission CO2"].fillna(df["Emission CO2"].median())
    df["Emission CO2"] = np.log1p(df["Emission CO2"])

    del df["Puissance nominale électrique"]
    del df["Conso elec"]
    del df["Autonomie elec"]
    del df["Autonomie elec urbain"]
    
    return df

def preprocessing(df):
    df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
    del df_test
    df_train = df_train.reset_index(drop=True)

    y_train = df_train["Emission CO2"].values

    del df_train['Emission CO2']
    train_dicts = df_train.to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dicts)
    
    return dv, X_train, y_train

def train_model(X_train, y_train):
    rf = RandomForestRegressor(random_state=42,
                            bootstrap = True,
                            n_estimators = 110,
                            max_depth = 12,
                            min_samples_leaf = 2,
                            min_samples_split = 3,
                            n_jobs=-1)
    rf.fit(X_train, y_train)
    
    return rf