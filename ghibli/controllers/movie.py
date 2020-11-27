"""
module documentation
"""
import logging
from cachetools import cached, TTLCache
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ghibli.services.composite_service import CompositeService


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@cached(cache=TTLCache(maxsize=1024, ttl=10))
def fetch_all_movies():
    """
    Fetch all movies
    """
    logging.info('Into fetch_all_movies - Cached')
    composite_service = CompositeService()
    movies_list = composite_service.fetch_all_movies()
    return movies_list

@router.get("/movies", response_class=HTMLResponse)
def movies(request: Request):
    """
    List of movies
    """
    logging.info('Into movies endpoint')
    cached_data = fetch_all_movies()
    return templates.TemplateResponse("movies.html", {"request" : request, "movies" : cached_data})
