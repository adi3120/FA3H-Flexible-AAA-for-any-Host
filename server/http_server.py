from fastapi import FastAPI
from pydantic import BaseModel
from core.auth_service import authenticate

app = FastAPI()


class AuthRequest(BaseModel):
    username: str
    password: str


@app.post("/authenticate")
def authenticate_user(request: AuthRequest):
    result = authenticate(request.username, request.password)
    return result