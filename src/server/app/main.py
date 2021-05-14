from routes import homepage_blueprint, prediction_blueprint
from flask import Flask, redirect, url_for

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

app.register_blueprint(homepage_blueprint, url_prefix='')
app.register_blueprint(prediction_blueprint, url_prefix='/api')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = app.config['PORT'], debug = False)