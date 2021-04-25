import requests
from GitHubRepository import GitHubRepository
URL = "https://api.github.com"


class GitHubUser:
    def __init__(self, name: str):
        self.name = name
        self.valid = self.validate_username()
        if self.valid:
            self.repositories = self.import_repositories()
            self.total_stars_count = self.count_stars()

    def validate_username(self):
        r = requests.get(url=f"{URL}/users/{self.name}")
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            return False
        return True

    def import_repositories(self):
        repos = self.request_repositories()
        return self.convert_repos(repos)

    def request_repositories(self):
        repos = []
        page_number = 0
        while True:
            page_number += 1
            response = requests.get(url=f"{URL}/users/{self.name}/repos?per_page=100&page={page_number}").json()
            if response:
                repos += response
            else:
                return repos

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

    def get_total_stars_count(self):
        return self.total_stars_count

    def is_valid(self):
        return self.valid
