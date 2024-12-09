from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    from curso_flask.forms.app import routers

    routers.init_app(app)

    return app

