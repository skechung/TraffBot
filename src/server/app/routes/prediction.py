from flask import Blueprint, jsonify

prediction_blueprint = Blueprint('prediction', __name__)

@prediction_blueprint.route('/prediction', methods=['GET'])
def prediction():
    """Make a new prediction against the trained model
    """
    return jsonify({'data': {'prediction': 0}})
