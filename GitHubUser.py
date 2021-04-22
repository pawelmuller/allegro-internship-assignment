import requests
from GitHubRepository import GitHubRepository
URL = "https://api.github.com"


class GitHubUser:
    def __init__(self, name: str):
        self.name = name
        self.repositories = self.import_repositories()
        self.summed_stars_count = None

    def import_repositories(self):
        repos = requests.get(url=f"{URL}/users/{self.name}/repos").json()
        return repos

