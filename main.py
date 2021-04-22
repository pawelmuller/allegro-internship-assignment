from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/git/{username}/repos")
async def get_repos(username: str):
    return {"username": f"{username}"}


@app.get("/git/{username}/stars")
async def get_stars(username: str):
    return {"username": f"{username}"}
