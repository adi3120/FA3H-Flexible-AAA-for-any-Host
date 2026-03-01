from fastapi import FastAPI
from pydantic import BaseModel
from core.auth_service import authenticate
from utils.logger import get_logger

app = FastAPI()
logger = get_logger(__name__)


class AuthRequest(BaseModel):
    username: str
    password: str


@app.post("/authenticate")
def authenticate_user(request: AuthRequest):
    logger.info(f"Auth attempt for user: {request.username}")
    result = authenticate(request.username, request.password)

    if result["success"]:
        logger.info(f"Authentication success for user: {request.username}")
    else:
        logger.warning(
            f"Authentication failed for user: {request.username} | Reason: {result.get('reason')}"
        )
    return result