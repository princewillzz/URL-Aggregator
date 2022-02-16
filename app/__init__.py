from flask import Flask


def create_app():

    # Define the WSGI application object
    app = Flask(__name__)


    # Configurations
    app.config.from_object('config')
    app.url_map.strict_slashes = False

    return app
