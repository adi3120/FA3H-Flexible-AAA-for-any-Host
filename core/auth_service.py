import bcrypt
from db.models import get_user_by_username


def authenticate(username: str, password: str) -> dict:
    user = get_user_by_username(username)

    if not user:
        return {"success": False, "reason": "User not found"}

    if not user["is_active"]:
        return {"success": False, "reason": "User inactive"}

    stored_hash = user["password_hash"].encode()

    if bcrypt.checkpw(password.encode(), stored_hash):
        return {"success": True, "role": user["role"]}
    else:
        return {"success": False, "reason": "Invalid credentials"}