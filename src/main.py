"""API Endpoints"""
from fastapi import FastAPI, HTTPException, status
from .config import log ,VERSION

app = FastAPI()


@app.get("/")
def welcome():
    """Root Endpoint returns a welcome message"""
    return {"message": "Welcome to DevOps Project"}

@app.get("/version")
async def version():
    """Endpoint returns the current API version"""
    if VERSION:
        return {"version": VERSION}
    log.warning("Request to Version endpoint responsed with an 500 error")
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Service configuration unavailable"
        )
    