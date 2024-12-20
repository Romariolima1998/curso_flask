

from flask import render_template, redirect, url_for, flash
from flask_login import  current_user

from curso_flask.blueprints.app.models import  Book
from curso_flask.blueprints.app import db
from curso_flask.blueprints.app.forms import  BookForm, UserBookForm
from curso_flask.blueprints.app.book import book


@book.route('/book/add/', methods=['GET', 'POST'])
def book_add():
    form = BookForm()

    if form.validate_on_submit():
        book = Book()
        book.name = form.name.data

        db.session.add(book)
        db.session.commit()

        flash('Livro cadastrado com sucesso', 'success')
        return redirect(url_for('.book_add'))

    return render_template('book/add.html', form=form)

@book.route('/user/<int:id>/add-book', methods=['GET', 'POST'])
def user_add_book(id):
    form = UserBookForm()
    if form.validate_on_submit():
        book = Book.query.get(form.book.data)
        current_user.books.append(book)

        db.session.add(current_user)
        db.session.commit()

        flash('Livro cadastrado com sucesso', 'success')
        return redirect(url_for('.user_add_book', id=id))

    return render_template('book/user_add_book.html',form=form)