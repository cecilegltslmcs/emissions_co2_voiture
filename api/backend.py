import pickle
import numpy as np
from fastapi import FastAPI

def load_model(INPUT_FILE):
    with open(INPUT_FILE) as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

app = FastAPI()

INPUT_FILE = "../models/random_forest.bin"

dv, model = load_model(INPUT_FILE)

@app.get('/')
def home():
    return "Bienvenue sur l'application de prédiction de consommation de CO2"

@app.post("/predict")
def predict(car):
    X = dv.transform([car])
    y_pred = np.expm1(model.predict(X)).round(2)
    
    return y_pred
    