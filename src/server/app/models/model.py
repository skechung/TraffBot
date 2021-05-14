import pandas as pd
import numpy as np
import pickle
import os
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error


# Convert Start_Time into hours 
def get_time(row):
    return round(row['Start_Time'].hour + row['Start_Time'].minute / 60, 1)


if (os.path.exists('trained_model.pickle')):
    # We already have an existing model and we can use it to make a prediction
    model = pickle.load(open('trained_model.pickle', 'rb'))
    mean = pickle.load(open('model_mean_values', 'rb'))
    var = pickle.load(open('model_var_values', 'rb'))
    print(model)
    print(mean)
    print(var)

else:
    # Create a new model and train it

    # Load in the data (this is relative to Harjot's path of the data)
    # Shouldn't pose any issues since the model should already have been trained.
    print('Loading in CSV...')
    df = pd.read_csv('../../../US_Accidents_Dec20.csv')
    print('Done loading in CSV...')

    # Narrow by only CA
    df = df[df['State'] == 'CA']

    # Convert Start Time and End Time to DateTime objs
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='%Y-%m-%d %H:%M:%S')
    df['End_Time'] = pd.to_datetime(df['End_Time'], format='%Y-%m-%d %H:%M:%S')

    # Add the collision duration
    df['duration_in_mins'] = (df['End_Time'] - df['Start_Time']).dt.total_seconds() / 60

    # Apply get_time function to Start_Time
    df['Start_Time'] = df.apply(get_time, axis=1)

    # Drop collisions lasting longer than 6 hours
    df = df[df['duration_in_mins'] <= 360]
    print(f'Size after dropping collisions lasting longer than 6 hours: {df.shape[0]}')

    # Narrow down df to consist only of top 5 features (from feature selection)
    # and the target variable (duration_in_mins)
    df = df[['Start_Lat', 'Start_Time', 'Humidity(%)', 'Temperature(F)', 'Wind_Speed(mph)', 'duration_in_mins']]
    
    # Drop rows with NaN values
    print(f'Number of rows before dropping NaN rows: {df.shape[0]}')
    df.dropna(inplace=True)
    print(f'Number of rows after dropping NaN rows: {df.shape[0]}')
    

    print('Detecting outliers...')
    # Remove outliers from the dataframe
    detector = IsolationForest(n_jobs=-1)
    outliers = detector.fit_predict(df)

    print('Removing outliers...')
    df.reset_index(drop=True,inplace=True)
    
    if_outcome = np.where(outliers == -1)
    print(f'Size before dropping outliers: {df.shape[0]}')
    
    df.drop(if_outcome[0], inplace=True)
    print(f'Size after dropping outliers: {df.shape[0]}')

    # Create dependent and independent dataframes
    X = df.drop(['duration_in_mins'], axis=1)
    Y = df['duration_in_mins']

    # Standard scale on X
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)
    X = pd.DataFrame(scaled_features, columns=X.columns)

    # Need to save the variance and mean of the scaler
    # so that we can use those same values to scale new inputs
    print(f'Scaler\'s mean values: {scaler.mean_}')
    print('Pickling the mean values...')
    with open('model_mean_values', 'wb') as f:
        pickle.dump(scaler.mean_, f)
    print('Done pickling the mean values...')
    
    print(f'Scaler\'s variance values: {scaler.var_}')
    print('Pickling the variance values...')
    with open('model_var_values', 'wb') as f:
        pickle.dump(scaler.var_, f)
    print('Done pickling the variance values...')


    # Create the MLP model
    print('Training the MLP model...')
    model = MLPRegressor(hidden_layer_sizes = (4,5,6), activation = "relu", solver="adam", batch_size=32, learning_rate_init=.001).fit(X, Y)
    print('Model is done training...')

    print('Finding MSE on training data...')
    pred = model.predict(X)
    mse = mean_squared_error(Y, pred, squared=False)
    print("Model MSE: ", mse)

    print('Pickling the model...')
    with open('trained_model.pickle', 'wb') as f:
        pickle.dump(model, f)
    print('Done pickling the model...')

    print('Model training complete')