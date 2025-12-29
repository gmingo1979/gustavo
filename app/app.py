from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = app.config.get('SECRET_KEY')

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/testing")
    def testing():
        return "<p>Producción</p>"