import os
from dotenv import load_dotenv

load_dotenv()

# ---- Server Config ------------ #
PORT = 443 # Port of the Server
# ---- Server Config Ends ------- #
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

MODEL_PICKLE_PATH='./models/trained_model.pickle'
MEAN_PICKLE_PATH='./models/model_mean_values.pickle'
VARIANCE_PICKLE_PATH='./models/model_var_values.pickle'