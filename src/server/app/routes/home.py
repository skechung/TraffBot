from flask import Blueprint, request, Response, render_template, \
    make_response, send_from_directory, current_app

homepage_blueprint = Blueprint('home', __name__)

@homepage_blueprint.route('/', methods=['GET'])
@homepage_blueprint.route('/home', methods=['GET'])
def home():
    """Render the homepage
    """
    return render_template('home.jinja2')
