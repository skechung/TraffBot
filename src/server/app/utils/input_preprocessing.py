import pickle 
import numpy as np
from sklearn.neural_network import MLPRegressor

def make_prediction(lat, start_time, humidity, temp, wind_speed):
    feature = [lat, start_time, humidity, temp, wind_speed]
    model = pickle.load(open('../server/app/model/trained_model.pickle', 'rb'))
    mean = pickle.load(open('../server/app/model/model_mean_values', 'rb'))
    var  = pickle.load(open('../server/app/model/model_var_values', 'rb'))

    scaled_features = []
    # Scale each feature
    for i in range(len(feature)):
        scaled_features.append((feature[i]-mean[i]) / var[i])

    return model.predict(np.array(scaled_features).reshape(1,-1))[0]

def time_scalar():
    pass