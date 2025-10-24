"""Module providing logging functionalities."""
import logging
from fastapi import FastAPI, HTTPException, status

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
def welcome():
    """Root Endpoint returns a welcome message"""
    return {"message": "Welcome to DevOps Project"}

@app.get("/version")
async def version():
    """Endpoint returns the current API version"""
    try:
        with open(file="VERSION", mode="r", encoding="utf-8") as version_file:
            return {"version": version_file.read().strip()}
    except FileNotFoundError as e:
        logger.error(" File Not Found : %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) from e
    except PermissionError as e:
        logger.error(" Permission Denied : %s", str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR) from e
