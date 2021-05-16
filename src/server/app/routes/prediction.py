from flask import Blueprint, jsonify, request

from engines.crash_time_regressor import CrashTimeRegressor
crash_time_regressor = CrashTimeRegressor()

prediction_blueprint = Blueprint('prediction', __name__)

@prediction_blueprint.route('/prediction', methods=['POST'])
def prediction():
    """Make a new prediction against the trained model
    """

    data = request.get_json()
    data = list(data.values())
    predicted_time = crash_time_regressor.predict(data)

    return jsonify({'data': {'prediction': round(predicted_time)}})
