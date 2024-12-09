from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from curso_flask.blueprints.app.models import User
from curso_flask.blueprints.app import db
from curso_flask.blueprints.app.forms import LoginForm, RegisterForm
from curso_flask.blueprints.app.auth import auth



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.password = generate_password_hash(form.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users.index'))

    return render_template('register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.index'))
    


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember = form.remember.data


        user =User.query.filter_by(email=email).first()
        if not user:
            flash('credencias invalidas', 'danger')
            return redirect(url_for('auth.login'))
        
        if not check_password_hash(user.password, password ):
            flash('credencias invalidas', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user,remember=remember, duration=timedelta(days=7))
        return redirect(url_for('users.index'))

    return render_template('login.html', form=form)
