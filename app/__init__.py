from flask import Flask
from flask_bootstrap import bootstrap


def create_app():
    app = Flask(__name__)
    bootstrap = Bootsrapt(app)
    app.config['SECRET_KEY'] = 'SUPER SECRETO'

    return app