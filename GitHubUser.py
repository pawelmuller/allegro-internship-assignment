import requests
from GitHubRepository import GitHubRepository
URL = "https://api.github.com"


class GitHubUser:
    def __init__(self, name: str):
        self.name = name
        self.repositories = self.import_repositories()
        self.total_stars_count = self.count_stars()

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

    def count_stars(self):
        counter = 0
        for repository in self.repositories:
            counter += repository.get_stars_count()
        return counter

    def get_repositories(self):
        return self.repositories
