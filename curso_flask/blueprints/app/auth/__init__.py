from flask import Blueprint


auth = Blueprint('auth', __name__)

from curso_flask.blueprints.app.auth import views