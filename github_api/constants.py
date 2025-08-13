BASE_URL = "https://api.github.com"

ENDPOINTS = {
    "REPOS": "/users/{username}/repos",
    "PRS": "/search/issues?q=is:pr+author:{username}"
}