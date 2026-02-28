import mysql.connector
from utils.config import DB_CONFIG


def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        raise RuntimeError(f"Database connection failed: {err}")