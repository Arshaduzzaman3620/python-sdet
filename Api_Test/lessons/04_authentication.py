"""
Lesson 04 - Basic authentication
  - Passing auth=(user, password) to requests
  - Reading the secret from an environment variable, not from code

Set the password first (in the same terminal):
    export GITHUB_PASSWORD="your-token"

Run from the Api_Test folder:
    python -m lessons.04_authentication
"""
import requests

from utilities.configurations import getPassword

url = "https://api.github.com/user"
github_response = requests.get(url, verify=False, auth=('rahulshettcademy', getPassword()))

print(github_response.status_code)
