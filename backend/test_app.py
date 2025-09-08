import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        # Setup a test user in the database
        with app.app_context():
            db.create_all()
            if not User.query.filter_by(username='testuser').first():
                user = User(username='testuser', password='testpass')
                db.session.add(user)
                db.session.commit()
        yield client
        # Teardown
        with app.app_context():
            db.drop_all()

def test_home_redirect_not_logged_in(client):
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'<h2>Login</h2>' in response.data

def test_home_redirect_logged_in(client):
    with client.session_transaction() as sess:
        sess['user'] = 'testuser'
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b'Network Traffic Dashboard' in response.data

def test_login_success(client):
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpass'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Network Traffic Dashboard' in response.data

def test_login_failure(client):
    response = client.post('/login', data={
        'username': 'wronguser',
        'password': 'wrongpass'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid credentials' in response.data
