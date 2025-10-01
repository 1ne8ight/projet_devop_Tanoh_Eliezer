import pytest

from application.routes import addition, app


def test_addition():
    assert addition(2, 5) == 7
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"7" in response.data
