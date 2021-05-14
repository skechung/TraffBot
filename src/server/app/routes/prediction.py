from flask import Blueprint, jsonify, request

prediction_blueprint = Blueprint('prediction', __name__)

@prediction_blueprint.route('/prediction', methods=['POST'])
def prediction():
    """Make a new prediction against the trained model
    """
    print(request.get_json())

    return jsonify({'data': {'prediction': 0}})
