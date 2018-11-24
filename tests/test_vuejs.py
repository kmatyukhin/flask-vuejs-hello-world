import pytest
from vuejs import app


@pytest.fixture
def client():
    client = app.test_client()

    yield client


def test_messages(client):
    """Test that messages work."""

    rv = client.get('/')
    assert b'id="app"' in rv.data
