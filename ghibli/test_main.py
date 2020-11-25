"""
Module documentation
"""
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_read_main():
    """
    Testing root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    response = client.get("/movies")
    assert response.status_code == 200
    assert len(response.text) > 100
