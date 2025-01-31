"""Entry point of the development application

This module is the entry point of the development application. It creates the FastAPI
"""

from fastapi import FastAPI
import uvicorn
from .routers import hello as hello_router

app: FastAPI = FastAPI()

app.include_router(
    hello_router.router,
    tags=["hello"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
