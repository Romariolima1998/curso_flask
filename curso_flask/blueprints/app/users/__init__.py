from flask import Blueprint

users = Blueprint('users', __name__)

from curso_flask.blueprints.app.users import views