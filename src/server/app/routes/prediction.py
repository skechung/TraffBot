from flask import Blueprint, jsonify

prediction_blueprint = Blueprint('prediction', __name__)


@prediction_blueprint.route('/prediction', methods=['GET'])
def home():
    """Download a book
    """
    return jsonify({'data': {'prediction': 0}})
