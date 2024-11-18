from flask import Flask, render_template, flash
from datetime import datetime
from curso_flask.template import filters


app = Flask(__name__, template_folder='pasta_templates',static_folder='public')
app.config['SECRET_KEY'] = 'secret'

app.jinja_env.filters['format_date'] = filters.format_date


@app.route('/templates')
def templates():
    
    flash('created user success')

    return render_template('index.html')


@app.route('/users')
def users():
    flash('essa e a pagina de usuario', 'warning')

    usuarios =[{
        'name': 'joao marcos',
        'idade': 100,
        'email': 'joao@marcos.com',
        'active': False,
        'since': datetime.utcnow()

    },
    {
        'name': 'roberta',
        'idade': 100,
        'email': 'roberto@marcos.com',
        'active': True,
        'since': datetime.utcnow()

    }]

    return render_template('users.html', users=usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=8000)