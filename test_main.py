import pytest
from fastapi.testclient import TestClient
from main import app
from GitHubRepository import GitHubRepository
from GitHubUser import GitHubUser
import requests

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world!"}


def test_extraction():
    test_dict = {"name": "Arthur", "stargazers_count": 15}
    assert GitHubRepository.extract_name(test_dict) == "Arthur"
    assert GitHubRepository.extract_stars_count(test_dict) == 15


def test_import_repositories():
    user = GitHubUser("apple")
    response = requests.get("https://api.github.com/users/apple/repos")
    request_repos = GitHubUser.convert_repos(response.json())

    for user_repo, request_repo in zip(user.repositories, request_repos):
        assert user_repo.name == request_repo.name
        assert user_repo.stars_count == request_repo.stars_count


@pytest.mark.parametrize("repo, name, stars_count",
                         [
                             ({
                                 "name": "Elizabeth",
                                 "rest of names": "Alexandra Mary",
                                 "title": "Her Majesty The Queen",
                                 "stargazers_count": 999999999
                             }, "Elizabeth", 999999999), ({
                                 "name": "Peter Parker",
                                 "alter-ego": "Spider-Man",
                                 "has brown eyes": "who knows",
                                 "stargazers_count": 1500
                             }, "Peter Parker", 1500), ({
                                 "name": "Cleopatra",
                                 "preferred bathing fluid": "milk",
                                 "stargazers_count": 7
                             }, "Cleopatra", 7)
                         ])
def test_convert_repositories(repo, name, stars_count):
    converted_repo = GitHubUser.convert_repos([repo])
    converted_repo = converted_repo[0]
    assert converted_repo.name == name
    assert converted_repo.stars_count == stars_count


@pytest.mark.parametrize("username, response_code",
                         [("pawelmuller", 200), ("apple", 200), ("SomeNotSoRandomlyChosenName987", 404)])
def test_response_codes(username, response_code):
    response = client.get(f"/git/users/{username}")
    assert response.status_code == response_code
