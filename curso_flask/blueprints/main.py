from curso_flask.blueprints.app import create_app, db
from curso_flask.blueprints.app.models import User, Profile, Book

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Profile': Profile, 'Book': Book}

if __name__ == '__main__':
    app.run(debug=True, port=8000)