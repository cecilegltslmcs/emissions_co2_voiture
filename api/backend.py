import pickle
import numpy as np
from fastapi import FastAPI

app = FastAPI()

INPUT_FILE = "models/random_forest.bin"

def load_model(INPUT_FILE):
    with open(INPUT_FILE) as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

@app.get('/')
def home():
    return "Bienvenue sur l'application de prédiction de consommation de CO2"

@app.post("/predict")
def predict(car:dict):
    dv, model = load_model(INPUT_FILE)
    X = dv.transformer([car])
    y_pred = np.expm1(model.predict(X)).round(2)
    
    return y_pred
    