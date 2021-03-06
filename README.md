# Simple GitHub API

## Features
Application implements a very simple GitHub API that allows listing user's public repositories and checking number of
stars (for each and total).


### Available endpoints
 - `GET` `/git/users/{username}` - allows getting all information about user, such as name, validity,
   list of public repositories and total stars count
 - `GET` `/git/users/{username}/repos` - allows getting list of all user's public repositories
 - `GET` `/git/users/{username}/stars` - allows getting total number of stars in user's public repositories


### Additionally, each endpoint returns:
 - `200 "OK"` status code if everything is ok
 - `404 "Not Found"` status code if given username does not belong to any user
 - `404 "Not Found"` status code if given user exists, but has no public repositories




## How to install?
Here are a few steps that will allow you to run the application:
1. First, you need to check whether you have Python (version 3.8 or newer).
   Python can be found [here](https://www.python.org/downloads/).
2. It is recommended to use separate virtual environment for convenience.
If you would like to use one, please follow instructions from official
   [Python docs](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments).
3. In order to work properly application needs to meet requirements from `requirements.txt`. To satisfy that demand run:
    ```
   python -m pip install -r requirements.txt
    ```



## How to run?
That one's easy. If you have followed the installation process and have all requirements satisfied - just run:
```
    uvicorn main:app
```



## Future development
In the future the application could be expanded with following features:

 - A user-friendly interface that would allow using API's features visually (but that's more of front-end development,
   tho)
 - More endpoints thet would implement new features, e.g. listing user's followers or listing who user follows
 - A temporary cache: not only would we save some requests (since GitHub API has limits per IP per day), but also it
   would be faster (we would request a built-in database instead of some distant source from the internet)

