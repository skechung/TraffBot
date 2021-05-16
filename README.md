# ECS171Project

## **Summary**
Using a dataset of 4.2 million U.S car accidents, we wish to explore the connections between time of crash, road conditions, and road features, and the severity of car accidents (in relation to how long it takes to clear the traffic accident). This data set is from [Kaggle](https://www.kaggle.com/sobhanmoosavi/us-accidents?select=US_Accidents_Dec20.csv), and has 48 different variables. It is important to note this data is only for 49 states, so it might not be able to be applied on data outside of the United States.

## **Project Schema**
The repository is structured via the following schema:

- **src/notebooks/**
  - jupyter notebooks live here
- **src/datasets/**
  - the datasets live here
- **src/server/**
  - code related to the website & demo lives here
- **src/fe_scripts/**
  - code related scripts in regards to feature engineer live here
- **tests/**
  - unit, integration, and other QA testing scripts live here
  - 
## **Configuration**
Configuration options need to be set based on whether the model is run locally or deployed via Docker.

### `.env` File
A dotfile called `.env` needs to be created or copied from the included `.env-default` file. Settings in the `.env` include:

- **WEATHER_API_KEY=** key to use the OpenWeather API tool for retrieving metadata from GPS cords. Read more about how to get the API key [here]('https://openweathermap.org/appid').
- **SSL_CERT_PATH=** path to a ssl certificate file to be used when deploying with Docker. Make sure to not put a passphase on the certificate. Example `/etc/ssl/certs/cert.pem`. 
- **SSL_CERT_KEY_PATH=** path to a ssl certificate key file to be used when deploying with Docker. Make sure to not put a passphase on the certificate. Example `/etc/ssl/certs/key.pem`.
- **NGROK_AUTH=** the API key when creating an ngrok account. Used as a proxy to expose the site to the world.

### `config.pg` File
Configuration of the server enviornment. Generally, these options dont need to be changed. Settings in the `config.py` include:
- **PORT=** the port on which the server should be run. Default 9000. Docker and the WSGI expect this port to be 9000. 
- **WEATHER_API_KEY=** the API key for OpenWeather API. By default it will be pulled from the `.env` file.
- **MODEL_PICKLE_PATH=** the path to the pickled MLPRegressor model. 
- **MEAN_PICKLE_PATH=** the path to the pickled mean for the MLPRegressor model.
- **VARIANCE_PICKLE_PATH=** he path to the pickled variance for the MLPRegressor model.

## **Installation**
Installation is based on whether the service would be run with Docker or not.

### Without Docker
1) Install python3.7+ onto the machine.
2) Install dependencies via `pip3 install -r requirements.txt`

### With Docker
1) Install Docker and make sure docker-compose is installed as well. If not, install docker-compose too.

## **Runtime**
To run the server, it depends if it is done through Docker or not. To run the server:

### Without Docker
1) Navigate to src/server/app
2) Register for OpenWeather API and put API key value in **WEATHER_API_KEY** (methoed in Configuration section).
3) To run without HTTPS, run as `python3 main.py`. Note that this method will not work as Geolocation API requires HTTPS. To run with HTTPS, run as `python3 main.py ssl`.

### With Docker
1) Make sure that certificates are setup and the path for **SSL_CERT_PATH** and **SSL_CERT_KEY_PATH** exists and the certs themselves dont have passphases. Also make sure Ngrok account exists and API key is placed in **NGROK_AUTH**.
2) Register for OpenWeather API and put API key value in **WEATHER_API_KEY** (methoed in Configuration section).
3) Build the containers via `docker-compose build`
4) Create and run the containers with `docker-compose up`.
5) Go to [Endpoints>Status](https://dashboard.ngrok.com/endpoints/status) on Ngrok's website and see the generated tunnels to access the site. Note that these tunnels change each time you run `docker-compose up`.