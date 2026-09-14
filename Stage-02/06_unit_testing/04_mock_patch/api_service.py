import requests

def get_user():
    response = requests.get("https://example.com/user")
    data = response.json()
    return data['name']