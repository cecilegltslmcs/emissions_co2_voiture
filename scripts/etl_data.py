import requests
import pandas as pd
import io
import sqlite3

def extract(url):
    r = requests.get(url)
    r.raise_for_status()
    data = r.content.decode("utf-8")
    df = pd.read_csv(io.StringIO(data))
    return df

def transform(df):
    df["Conso basse vitesse"] = ((df["Conso basse vitesse Max"] + df["Conso basse vitesse Min"]) / 2)
    df["Conso moyenne vitesse"] = ((df["Conso moyenne vitesse Max"] + df["Conso moyenne vitesse Min"]) / 2)
    df["Conso haute vitesse"] = ((df["Conso haute vitesse Max"] + df["Conso haute vitesse Min"]) / 2)
    df["Conso T-haute vitesse"] = ((df["Conso T-haute vitesse Max"] + df["Conso T-haute vitesse Min"]) / 2)
    df["Conso vitesse mixte"] = ((df["Conso vitesse mixte Max"] + df["Conso vitesse mixte Min"]) / 2)
    df["Conso elec"] = ((df["Conso elec Min"] + df["Conso elec Max"]) / 2)
    df["Autonomie elec"] = ((df["Autonomie elec Min"] + df["Autonomie elec Max"]) / 2)
    df["Autonomie elec urbain"] = ((df["Autonomie elec urbain Min"] + df["Autonomie elec urbain Max"]) / 2)

    df["Emission CO2"] = ((
    df["CO2 basse vitesse Min"] +
    df["CO2 basse vitesse Max"] +
    df["CO2 moyenne vitesse Min"] +
    df["CO2 moyenne vitesse Max"] +
    df["CO2 haute vitesse Min"] +
    df["CO2 haute vitesse Max"] +
    df["CO2 T-haute vitesse Min"] +
    df["CO2 T-haute vitesse Max"] +
    df["CO2 vitesse mixte Min"] +
    df["CO2 vitesse mixte Max"]
    ) / 10)

    del df["Conso basse vitesse Max"]
    del df["Conso basse vitesse Min"]
    del df["Conso moyenne vitesse Max"]
    del df["Conso moyenne vitesse Min"]
    del df["Conso haute vitesse Max"]
    del df["Conso haute vitesse Min"]
    del df["Conso T-haute vitesse Max"]
    del df["Conso T-haute vitesse Min"]
    del df["Conso vitesse mixte Max"]
    del df["Conso vitesse mixte Min"]

    del df["Conso elec Min"]
    del df["Conso elec Max"]
    del df["Autonomie elec Min"]
    del df["Autonomie elec Max"]
    del df["Autonomie elec urbain Min"]
    del df["Autonomie elec urbain Max"]

    del df["CO2 basse vitesse Min"]
    del df["CO2 basse vitesse Max"]
    del df["CO2 moyenne vitesse Min"]
    del df["CO2 moyenne vitesse Max"]
    del df["CO2 haute vitesse Min"]
    del df["CO2 haute vitesse Max"]
    del df["CO2 T-haute vitesse Min"]
    del df["CO2 T-haute vitesse Max"]
    del df["CO2 vitesse mixte Min"]
    del df["CO2 vitesse mixte Max"]

    del df["Libellé modèle"]
    del df["Description Commerciale"]
    del df["Groupe"]
    del df["Essai CO2 type 1"]
    del df["Essai HC"]
    del df["Essai Nox"]
    del df["Essai HCNox"]
    del df["Essai particules"]
    del df["Masse OM Min"]
    del df["Masse OM Max"]
    del df["Prix véhicule"]
    del df["Barème Bonus-Malus"]

    df["Marque"] = df["Marque"].replace({"ROLLS ROYC" : "ROLLS ROYCE",
                                         "LAMBORGHIN" : "LAMBORGHINI"})

    return df

def load(dataframe):
    conn = sqlite3.connect('./datasets/ademe_car_labeling.db')
    dataframe.to_sql("car_information", conn, if_exists='append')
    conn.close()

if __name__ == '__main__':
    url = "https://data.ademe.fr/data-fair/api/v1/datasets/ademe-car-labelling/lines?size=10000&page=1&format=csv"
    data_from_url = extract(url)
    transformed_data = transform(data_from_url)
    load(transformed_data)