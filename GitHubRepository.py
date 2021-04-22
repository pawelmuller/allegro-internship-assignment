class GitHubRepository:
    def __init__(self, raw_repository_json):
        self.name = self.extract_name(raw_repository_json)
        self.stars_count = self.extract_stars_count(raw_repository_json)

    @staticmethod
    def extract_name(raw_repository):
        return raw_repository["name"]

    @staticmethod
    def extract_stars_count(raw_repository):
        return raw_repository["stargazers_count"]
