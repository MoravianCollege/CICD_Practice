from practice.app import app


def test_get_foo():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/foo?bar=Hi&mub=iH')
    assert b'bar is Hi' in result.data
    assert b'mub is iH' in result.data

def test_get_missing_arg():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/foo?bar=Hi')
    assert result.status_code == 404
