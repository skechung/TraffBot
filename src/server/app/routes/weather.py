from flask import Blueprint, jsonify, request
from config import WEATHER_API_KEY
import requests

weather_blueprint = Blueprint('weather', __name__)

@weather_blueprint.route('/weather', methods=['GET'])
def weather():
    """Fetches weather data for performing predictions
    """
    
    latitude = request.args.get('lat')
    longitude = request.args.get('long')
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={WEATHER_API_KEY}&units=imperial'
    
    response = requests.get(weather_api)
    data = response.json()

    return jsonify(data)
