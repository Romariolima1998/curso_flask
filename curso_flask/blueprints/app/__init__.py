from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap4

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap4()

class DefaultConfig:
    SECRET_KEY = 'default-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True


def create_app(config_class=None):
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'secret'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['TEMPLATES_AUTO_RELOAD'] = True

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object(DefaultConfig)

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    from curso_flask.blueprints.app import routers

    routers.init_app(app)

    return app

