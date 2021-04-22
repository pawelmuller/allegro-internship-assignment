import requests
from GitHubRepository import GitHubRepository
URL = "https://api.github.com"


class GitHubUser:
    def __init__(self, name: str):
        self.name = name
        self.repositories = self.import_repositories()
        self.summed_stars_count = None

    def import_repositories(self):
        repos = self.request_repositories()
        return self.convert_repos(repos)

    def request_repositories(self):
        return requests.get(url=f"{URL}/users/{self.name}/repos").json()

    @staticmethod
    def convert_repos(raw_repos):
        repos = []
        for raw_repo in raw_repos:
            repo = GitHubRepository(raw_repo)
            repos.append(repo)
        return repos

    def get_repositories(self):
        return self.repositories
