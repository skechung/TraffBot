import pickle
import numpy as np
from sklearn.neural_network import MLPRegressor
import config
from utils import input_preprocessing 

class CrashTimeRegressor:
    def __init__(self):
        # Features must follow this order: 
        # 'Start_Lat', 'Start_Time', 'Humidity(%)', 'Temperature(F)', 'Wind_Speed(mph)'

        # Load in the model, and saved variances and means for scaling
        self.model = pickle.load(open(config.MODEL_PICKLE_PATH, 'rb'))
        self.var = pickle.load(open(config.VARIANCE_PICKLE_PATH, 'rb'))
        self.mean = pickle.load(open(config.MEAN_PICKLE_PATH, 'rb'))

    def predict(self, features):
        features =  input_preprocessing.scale(features, self.mean, self.var)

        return self.model.predict(np.array(features).reshape(1,-1))[0]

