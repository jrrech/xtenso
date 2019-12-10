import pytest
from xtenso import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING' : True})

    with app.test_client() as client:
        yield client

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    print (rv.data)
    assert b'Hello, World!' in rv.data
