"""
Web Endpoints tests
"""
import logging
from bs4 import BeautifulSoup
from .test_base import client

def test_movies_endpoint():
    """
    Test the '/movies' endpoint
    """
    logging.info("Test movie endpoint")
    response = client.get("/movies")
    assert response.status_code == 200
    assert len(response.text) > 100

    # validate the basic contents of HTML
    soup = BeautifulSoup(response.text, features="html.parser")
    tables = soup.find_all("table")
    # Check if there is only one table
    assert len(tables) == 1
    # Check if the table has data
    body = tables[0].find_all("tr")
    assert len(body) > 0
