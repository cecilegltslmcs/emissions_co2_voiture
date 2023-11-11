import pandas as pd
import json

INPUT_FILE = "../datasets/original_dataset.csv"
OUTPUT_PATH = "dict_car.txt"

def extract_data_from_dataset(input_file):
    df = pd.read_csv(input_file, sep=";")

    data_car = df[['Marque','Modèle', 'Energie', 'Carrosserie', 'Gamme']]
    data_car["Marque"] = data_car["Marque"].replace({"ROLLS ROYC" : "ROLLS ROYCE",
                                                     "LAMBORGHIN" : "LAMBORGHINI"})
    data_car = data_car[data_car["Energie"] != 'ELECTRIC']

    return data_car

car_model = extract_data_from_dataset(INPUT_FILE)
car_model.to_csv("data_car.csv", index=False)