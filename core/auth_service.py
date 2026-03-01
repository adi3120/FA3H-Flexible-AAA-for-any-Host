import bcrypt
from db.models import get_user_by_username
from utils.logger import get_logger

logger=get_logger(__name__)

def authenticate(username: str, password: str) -> dict:
    logger.debug(f"Fetching user: {username}")
    user = get_user_by_username(username)

    if not user:
        logger.warning(f"User not found: {username}")
        return {"success": False, "reason": "User not found"}

    if not user["is_active"]:
        logger.warning(f"Inactive user attempted login: {username}")
        return {"success": False, "reason": "User inactive"}

    stored_hash = user["password_hash"].encode()

    if bcrypt.checkpw(password.encode(), stored_hash):
        logger.info(f"Login success for user: {username}")
        return {"success": True, "role": user["role"]}
    else:
        logger.error(f"Login failed for user: {username}")
        return {"success": False, "reason": "Invalid credentials"}