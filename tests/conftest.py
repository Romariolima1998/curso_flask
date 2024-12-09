import pytest
from curso_flask.blueprints.app import create_app, db


class TestConfig():
    SECRET_KEY = 'test-secret-key'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


@pytest.fixture
def client():
    app = create_app(TestConfig)
    # app.config.update({
    #     "TESTING": True,
    # })
    # app.config.update({'SQLALCHEMY_DATABASE_URI': "sqlite:///:memory:"})

    with app.app_context():

        db.create_all()

        yield app.test_client()

        db.session.remove()
        db.drop_all()
        


@pytest.fixture
def db_test():
    return db

#  context = app.app_context()
#     context.push()
# context.pop()