from flask_wtf import FlaskForm
from wtforms.fields import SelectField, StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import length, email,DataRequired

from curso_flask.blueprints.app.models import Book

class LoginForm(FlaskForm):
    email = EmailField('email')
    password = PasswordField('senha')
    remember = BooleanField('permanecer conectado')
    submit = SubmitField('logar')


class RegisterForm(FlaskForm):
    name = StringField('nome completo', validators=[DataRequired('campo obrigatorio')])
    email = EmailField('email', validators=[email(), DataRequired('campo obrigatorio')])
    password = PasswordField('senha',validators=[DataRequired('campo obrigatorio'),length(3,12, 'range de 3 a 12 caractere')])
    submit = SubmitField('cadastrar')


class BookForm(FlaskForm):
    name = StringField('nome do livro', validators=[DataRequired('campo obrigatorio')])
    submit = SubmitField('salvar')


class UserBookForm(FlaskForm):
    book = SelectField('livro', coerce=int,)
    submit = SubmitField('salvar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices= [(book.id, book.name) for book in Book.query.all()]