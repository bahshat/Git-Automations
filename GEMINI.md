# Git-Automation Project Refactoring by Gemini

This document summarizes the key refactorings and improvements made to the `Git-Automation` project.

## Project Overview
The `Git-Automation` project is designed to interact with the GitHub API to list user repositories and pull requests.

## Initial State
The project initially consisted of a `config.yaml` file for configuration and a `get-repos.py` script containing all the logic for API calls and data presentation.

## Refactoring - `GithubManager` Class
The core logic for interacting with the GitHub API has been encapsulated within a `GithubManager` class.
-   The `__init__` method now handles the loading of configuration (username and token).
-   A private method `_call_github_api` was introduced to centralize HTTP requests to the GitHub API, including error handling for network issues and bad responses.

## Modularity & Separation of Concerns
To improve code organization and maintainability, the project structure has been modularized:
-   **`constants.py`**: A new module created to store global constants such as `BASE_URL` and a dictionary `ENDPOINTS` for various API endpoints.
-   **`utils.py`**: A new module containing utility functions, specifically `load_config` for loading the `config.yaml` file.
-   **`github_api/` package**: A new directory created to house the core API interaction logic (`get_repos.py`, `constants.py`, `utils.py`). This makes `github_api` an importable Python package.
-   **`demo.py`**: This script now serves as the primary caller module, demonstrating how to use the `GithubManager` class from the `github_api` package.

## Generic Data Retrieval
-   A generic method `list_github_data` was introduced in `GithubManager`. This method takes an `endpoint_key` (e.g., "REPOS", "PRS") and fetches the corresponding data from the GitHub API.
-   `list_github_data` is designed to return a tuple `(data, error_message)`. `data` will be the API response (or an empty list if no data is found), and `error_message` will be `None` on success or a string describing the error.
-   The caller (`demo.py`) is responsible for any specific data extraction or post-processing (e.g., extracting the `"items"` list for pull requests).

## Error Handling
-   The `_call_github_api` method now uses `try-except` blocks to catch `requests.exceptions.RequestException` and returns an error message instead of exiting the program.
-   `list_github_data` checks for errors returned by `_call_github_api` and also returns an empty list if no data is found, ensuring a consistent return type for the caller.
-   The caller (`demo.py`) is responsible for checking the `error` part of the returned tuple and displaying appropriate messages.

## Code Style & Best Practices
-   **Guard Clauses**: The `demo.py` script was refactored to use guard clauses (early exits) for error handling and empty data checks, improving readability and reducing nested `if-else` statements.
-   **Linting**: The `ruff` linter was integrated to enforce code style and identify potential issues. All identified linting errors (unused imports) were fixed.

## Virtual Environment Management
-   The virtual environment (`.venv`) was recreated and necessary dependencies (`requests`, `PyYAML`, `ruff`) were reinstalled to resolve execution issues.
