from flask import Blueprint

book = Blueprint('book', __name__)

from curso_flask.blueprints.app.book import views