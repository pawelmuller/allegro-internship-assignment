import requests
from GitHubRepository import GitHubRepository
URL = "https://api.github.com"


class GitHubUser:
    def __init__(self, name):
        self.name = name
        self.repositories = None
        self.star_count = None
