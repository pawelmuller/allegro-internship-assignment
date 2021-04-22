# import pytest
from fastapi.testclient import TestClient
from main import app
from GitHubRepository import GitHubRepository

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_extraction():
    test_dict = {"name": "Arthur", "stargazers_count": 15}
    assert GitHubRepository.extract_name(test_dict) == "Arthur"
    assert GitHubRepository.extract_stars_count(test_dict) == 15
