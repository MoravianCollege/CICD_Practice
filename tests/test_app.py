from practice.app import app


def test_get_foo():
    app.config['TESTING'] = True
    client = app.test_client()

    result = client.get('/foo?bar=Hi')
    assert b'bar is Hi' in result.data
