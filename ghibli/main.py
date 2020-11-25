"""
module documentation
"""
import logging
from fastapi import FastAPI
from ghibli.controllers import movie


# Create and configure the FastAPI application
app = FastAPI()
app.include_router(movie.router)

# Configuration the application logger
logging.basicConfig(level=logging.DEBUG)
