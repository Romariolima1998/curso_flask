
from flask import render_template, redirect, url_for, flash
from flask_login import  login_required

from curso_flask.blueprints.app.models import User, Book
from curso_flask.blueprints.app import db
from curso_flask.blueprints.app.forms import LoginForm, RegisterForm, BookForm, UserBookForm
from curso_flask.blueprints.app.auth import auth as auth_blueprint
from curso_flask.blueprints.app.book import book as book_blueprint
from curso_flask.blueprints.app.users import users as users_blueprint

def init_app(app):
    app.register_blueprint(auth_blueprint)

    app.register_blueprint(book_blueprint)

    app.register_blueprint(users_blueprint)

   
    
    
    

    