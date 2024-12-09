from curso_flask.blueprints.app.models import User


def test_if_users_page_return_status_code_200(client):

    response = client.get('/')

    assert response.status_code == 200


def test_if_register_link_exists(client):
    response = client.get('/')

    assert 'register' in str(response.data)


def test_if_login_link_exists(client):
    response = client.get('/')

    assert 'login' in response.data.decode()

def test_register_user(client):
    data = {
        'name': 'amanda',
        'email': 'amanda@email.com',
        'password': 'amanda'
    }

    response = client.post('/register', data=data, follow_redirects=True)

    assert 'amanda' in response.data.decode()


def test_login_user(client, db_test):
    data = {
        'name': 'amanda',
        'email': 'amanda@email.com',
        'password': 'amanda'
    }

    response = client.post('/register', data=data, follow_redirects=True)

    data = {
        'email': 'amanda@email.com',
        'password': 'amanda'
    }

    response2 = client.post('/login', data=data, follow_redirects=True)

    assert 'logout' in response2.data.decode()