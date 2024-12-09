
from flask import render_template, redirect, url_for
from flask_login import  login_required

from curso_flask.blueprints.app.models import User
from curso_flask.blueprints.app import db
from curso_flask.blueprints.app.users import users


@users.route('/')
def index():
    users = User.query.all()
    return render_template('users.html', users=users)

@users.route('/user/<int:id>')
@login_required
def detail(id):
    user = User.query.get(id)
    return render_template('user.html', user=user)


@users.route('/user/delete/<int:id>')
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
