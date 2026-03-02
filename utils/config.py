from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"

load_dotenv(env_path)

# --- App ---
APP_ENV = os.getenv("APP_ENV", "dev")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 8000))

# --- Logging ---
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# --- Database ---
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

# --- HTTP ---
AAA_HOST = os.getenv("AAA_HOST", "127.0.0.1")
AAA_PORT = int(os.getenv("AAA_PORT", 8000))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 5))

# --- RADIUS ---
RADIUS_CONFIG = {
    "host": os.getenv("RADIUS_HOST", "127.0.0.1"),
    "port": int(os.getenv("RADIUS_PORT", 1812)),
    "shared_secret": os.getenv("RADIUS_SHARED_SECRET", "supersecret").encode(),
}