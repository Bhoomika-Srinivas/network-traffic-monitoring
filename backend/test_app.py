import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_redirect_not_logged_in(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_redirect_logged_in(client):
    with client.session_transaction() as sess:
        sess['user'] = 'testuser'
    response = client.get('/')
    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']
