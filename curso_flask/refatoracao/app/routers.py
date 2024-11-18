from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required

from curso_flask.refatoracao.app.models import User
from curso_flask.refatoracao.app import db

def init_app(app):
    @app.route('/')
    def index():
        users = User.query.all()
        return render_template('users.html', users=users)

    @app.route('/user/<int:id>')
    @login_required
    def detail(id):
        user = User.query.get(id)
        return render_template('user.html', user=user)


    @app.route('/user/delete/<int:id>')
    def delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            user = User()
            user.name = request.form['name']
            user.email = request.form['email']
            user.password = generate_password_hash(request.form['password'])

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('register.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))
        


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            remember = request.form.get('remember')


            user =User.query.filter_by(email=email).first()
            if not user:
                flash('credencias invalidas')
                return redirect(url_for('login'))
            
            if not check_password_hash(user.password, password ):
                flash('credencias invalidas')
                return redirect(url_for('login'))
            
            login_user(user,remember=remember, duration=timedelta(days=7))
            return redirect(url_for('index'))

        return render_template('login.html')