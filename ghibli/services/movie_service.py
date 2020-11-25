"""
Movie Service module
"""
import logging
import requests
from requests.exceptions import HTTPError
from ghibli.config_parser import config_parser


class MovieService:
    """
    Class documentation
    """
    base_url = config_parser['Default']['BaseUrl']

    def fetch_all_movies(self, *fields, limit=250):
        """
        Fetch all movies
        """
        logging.debug("fetch all movie data")
        try:
            query_parameter = "limit=" + str(limit)
            if fields is not None:
                query_parameter += "&fields=" + ",".join(fields)
            print("query parameter: " + query_parameter)
            response = requests.get(self.base_url + '/films?' + query_parameter)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            logging.error('HTTP error occurred: %s', http_err)  # Python 3.6


    def fetch_movie(self, *fields, _id):
        """
        Fetch a movie detail
        """
        logging.debug("fetch the movie data")
        try:
            query_parameter = "/" + _id
            if fields is not None:
                query_parameter += "?fields=" + ",".join(fields)
            print("query parameter: " + query_parameter)

            response = requests.get(self.base_url + '/films' + query_parameter)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            logging.error('HTTP error occurred: %s', http_err)  # Python 3.6
