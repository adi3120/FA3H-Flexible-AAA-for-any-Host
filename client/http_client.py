from dotenv import load_dotenv
import os
import requests
from utils.logger import get_logger
from utils.config import AAA_HOST, AAA_PORT, REQUEST_TIMEOUT


SERVER_HOST = AAA_HOST
SERVER_PORT = AAA_PORT
TIMEOUT = REQUEST_TIMEOUT

logger = get_logger(__name__)

def login(username, password):
    url = f"http://{SERVER_HOST}:{SERVER_PORT}/authenticate"
    logger.info("Sending HTTP Post request")

    response = requests.post(
        url,
        json={"username": username, "password": password},
        timeout=TIMEOUT
    )
    return response.json()

if __name__ == "__main__":
    result = login("testuser", "1234")
    print(result)
