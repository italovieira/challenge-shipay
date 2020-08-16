from flask import Flask
from config import config
from .api import configure_api
from .models import configure as configure_db


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    configure_db(app)

    configure_api(app)

    return app
