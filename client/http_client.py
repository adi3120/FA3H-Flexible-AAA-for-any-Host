import requests

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

def login(username, password):
    url = f"http://{SERVER_HOST}:{SERVER_PORT}/authenticate"
    response = requests.post(
        url,
        json={"username": username, "password": password},
        timeout=5
    )
    return response.json()


if __name__ == "__main__":
    result = login("testuser", "1234")
    print(result)