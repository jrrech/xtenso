import pytest
from xtenso import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING' : True})

    with app.test_client() as client:
        yield client

def test_hello_world(client):
    rv = client.get('/')
    print (rv.data)
    assert b'Hello, World!' in rv.data

def test_unit_positive(client):
    rv = client.get('/8')
    print (rv.data)
    assert b'oito' in rv.data

def test_unit_negative(client):
    rv = client.get('/-7')
    print (rv.data)
    assert b'menos sete' in rv.data
