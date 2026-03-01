from dotenv import load_dotenv
import os
import requests
from utils.logger import get_logger

load_dotenv()

SERVER_HOST = os.getenv("AAA_HOST", "127.0.0.1")
SERVER_PORT = int(os.getenv("AAA_PORT", 8000))
TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 5))

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