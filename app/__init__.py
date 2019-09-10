from flask import Flask
from flask_bootstrap import bootstrap
from .config import Config

def create_app():
    app = Flask(__name__)
    bootstrap = Bootsrapt(app)
    app.config.from_object(Config)

    return app