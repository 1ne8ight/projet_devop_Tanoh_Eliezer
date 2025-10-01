import pytest
from application.routes import addition, soustraction, app


# Tests unitaires pour les fonctions
def test_addition():
    assert addition(2, 5) == 7
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0


def test_soustraction():
    assert soustraction(5, 2) == 3
    assert soustraction(2, 5) == -3
    assert soustraction(0, 0) == 0


# Fixture pour le client Flask
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# Test de la route index
def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    # Vérifie que le résultat de addition est bien dans le rendu HTML
    assert b"7" in response.data
