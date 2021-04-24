from fastapi import FastAPI, Response, status
from GitHubUser import GitHubUser

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/git/users/{username}", status_code=status.HTTP_200_OK)
async def get_repos(username: str, response: Response):
    user = GitHubUser(username)
    if user.is_valid():
        return user
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "User Not Found"}


@app.get("/git/users/{username}/repos", status_code=status.HTTP_200_OK)
async def get_repos(username: str, response: Response):
    user = GitHubUser(username)
    if user.is_valid():
        repositories = user.get_repositories()
        return repositories
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "User Not Found"}


@app.get("/git/users/{username}/stars", status_code=status.HTTP_200_OK)
async def get_stars(username: str, response: Response):
    user = GitHubUser(username)
    if user.is_valid():
        stars_count = user.get_total_stars_count()
        return {"total_stars_count": stars_count}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "User Not Found"}
