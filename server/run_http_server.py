import uvicorn
from server.http_server import app
from utils.config import APP_HOST, APP_PORT

if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)