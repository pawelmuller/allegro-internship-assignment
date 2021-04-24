from fastapi import FastAPI
from GitHubUser import GitHubUser

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/git/{username}/repos")
async def get_repos(username: str):
    user = GitHubUser(username)
    repositories = user.get_repositories()
    return repositories


@app.get("/git/{username}/stars")
async def get_stars(username: str):
    user = GitHubUser(username)
    stars_count = user.get_total_stars_count()
    return {"total_stars_count": stars_count}
