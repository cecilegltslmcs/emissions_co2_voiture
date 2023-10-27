# import librairies
import pickle
from utils import data_preparation, preprocessing, train_model

PATH = "datasets/dataset.csv"
OUTPUT_FILE = 'models/random_forest.bin'


df = data_preparation(PATH)
dv, X_train, y_train = preprocessing(df)
model = train_model(X_train, y_train)

with open(OUTPUT_FILE, 'wb') as f_out:
    pickle.dump((dv, model), f_out)