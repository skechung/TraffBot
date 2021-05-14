import pandas as pd

def scale(features, means, vars):
    scaled_features = []
    
    # Turn Start Time into datetime object  
    features[1] = pd.to_datetime(features[1], format='%H:%M:%S')

    # Turn Start Time into a float that represents collision start
    features[1] = round(features[1].hour + (features[1].minute / 60), 1)

    # Scale each feature
    for i in range(len(features)):
        scaled_features.append((features[i]-means[i]) / vars[i])

    return scaled_features
