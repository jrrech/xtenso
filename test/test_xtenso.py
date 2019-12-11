import pytest
from xtenso import create_app


@pytest.fixture
def client():
    app = create_app({'TESTING': True})
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
    assert rv.status_code == 400

    rv = client.get('/-100000')
    assert rv.status_code == 400

    rv = client.get('/99999')
    assert rv.status_code == 200
    assert b'noventa e nove mil e novecentos e noventa e nove' in rv.data

    rv = client.get('/-99999')
    assert rv.status_code == 200
    assert b'menos noventa e nove mil e novecentos e noventa e nove' in rv.data


def test_cojunction(client):
    rv = client.get('/9')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 1

    rv = client.get('/99')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 2

    rv = client.get('/999')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 3

    rv = client.get('/9999')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 4

    rv = client.get('/99999')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 5

    rv = client.get('/10')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 1

    rv = client.get('/100')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 1

    rv = client.get('/1000')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 1

    rv = client.get('/10000')
    assert rv.status_code == 200
    assert len(str(rv.data).split(' e ')) == 1


def test_bad_param(client):
    rv = client.get('/teste')
    assert rv.status_code == 400

    rv = client.get('/10,2')
    assert rv.status_code == 400


def test_zero(client):
    rv = client.get('/0')
    assert rv.status_code == 200
    assert b'zero' in rv.data


def test_exceeding_zeros(client):
    rv = client.get('/00001')
    assert rv.status_code == 200
    assert b'um' in rv.data

    rv = client.get('/0000000000000000000000000000013')
    assert rv.status_code == 200
    assert b'treze' in rv.data

    rv = client.get('/-000000000000000000000000099998')
    assert rv.status_code == 200
    assert b'menos noventa e nove mil e novecentos e noventa e oito' in rv.data


def test_zeros_in_between(client):
    rv = client.get('/-50004')
    assert rv.status_code == 200
    assert b'menos cinquenta mil e quatro' in rv.data


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
