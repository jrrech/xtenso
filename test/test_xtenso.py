import pytest
from xtenso import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING' : True})
    with app.test_client() as client:
        yield client

def test_positive(client):
    rv = client.get('/8')
    print (rv.data)
    assert b'oito' in rv.data

def test_negative(client):
    rv = client.get('/-7')
    print (rv.data)
    assert b'menos sete' in rv.data

def test_out_of_bounds_param(client):
    rv = client.get('/100000')
    assert rv.status_code == 404

    rv = client.get('/-90000')
    assert rv.status_code == 200
    assert b'menos noventa mil' in rv.data

def test_bad_param(client):
    rv = client.get('/teste')
    assert rv.status_code == 405

    rv = client.get('/10,2')
    assert rv.status_code == 405

def test_exceeding_zeros(client):
    rv = client.get('/00001')
    assert rv.status_code == 200
    assert b'um' in rv.data

def test_zeros_in_between(client):
    rv = client.get('/-50013')
    assert rv.status_code == 200
    assert b'menos cinquenta mil e treze' in rv.data

def test_cem_cento(client):
    rv = client.get('/23100')
    assert rv.status_code == 200
    assert 'vinte e três mil e cem'.encode() in rv.data

    rv = client.get('/23105')
    assert rv.status_code == 200
    assert 'vinte e três mil e cento e cinco'.encode() in rv.data

def test_examples(client):
    rv = client.get('/1')
    assert rv.status_code == 200
    assert b'um' in rv.data

    rv = client.get('/-1042')
    assert rv.status_code == 200
    assert b'menos mil e quarenta e dois' in rv.data

    rv = client.get('/-94587')
    assert rv.status_code == 200
    assert b'noventa e quatro mil e quinhentos e oitenta e sete' in rv.data
