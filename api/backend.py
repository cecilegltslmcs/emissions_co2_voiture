import pickle
import numpy as np
from fastapi import FastAPI

def load_model(input_path: str)-> (DictVectorizer, RandomForestRegressor):
    with open(input_path) as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

app = FastAPI()

INPUT_FILE = "../models/random_forest.bin"

dv, model = load_model(INPUT_FILE)

@app.get('/')
def home()-> str:
    return "Bienvenue sur l'application de prédiction de consommation de CO2"

@app.post("/predict")
def predict(car: dict) -> float:
    X = dv.transform([car])
    y_pred = np.expm1(model.predict(X)).round(2)

    return y_pred
