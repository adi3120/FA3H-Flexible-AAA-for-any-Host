from db.database import get_connection
from utils.logger import get_logger

logger=get_logger(__name__)

def get_user_by_username(username: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    logger.debug(f"Querying DB for user: {username}")

    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    if user:
        logger.debug(f"User record found for: {username}")
    else:
        logger.debug(f"No DB record for: {username}")

    cursor.close()
    conn.close()

    return user