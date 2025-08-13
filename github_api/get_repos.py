import requests
from github_api.constants import BASE_URL, ENDPOINTS
from github_api.utils import load_config

class GithubManager:
    
    def __init__(self):
        cfg = load_config()
        self.username = cfg["username"]
        self.token = cfg["token"]

    
    def _call_github_api(self, endpoint):
        url = f"{BASE_URL}{endpoint}"
        headers = {"Authorization": f"token {self.token}"}

        try:
            resp = requests.get(url, headers=headers)
            resp.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return resp.json(), None
        except requests.exceptions.RequestException as e:
            return None, f"API error: {e}"

    
    def list_github_data(self, endpoint_key):
        endpoint = ENDPOINTS[endpoint_key].format(username=self.username)
        data, error = self._call_github_api(endpoint)

        if error:
            return None, error

        if not data:
            return [], None
        
        return data, None