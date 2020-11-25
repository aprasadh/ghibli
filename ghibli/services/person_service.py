"""
Movie Service module
"""
import logging
import requests
from requests.exceptions import HTTPError
from ghibli.config_parser import config_parser


class PersonService:
    """
    Person Service
    """
    base_url = config_parser['Default']['BaseUrl']

    def fetch_all_people(self, *fields, limit=250):
        """
        Fetch all people data
        """
        logging.debug("fetch all people data")
        try:
            query_parameter = "limit=" + str(limit)
            if fields is not None:
                query_parameter += "&fields=" + ",".join(fields)
            print("query parameter: " + query_parameter)

            response = requests.get(self.base_url + '/people?' + query_parameter)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            logging.error('HTTP error occurred: %s', http_err)  # Python 3.6

    def fetch_people(self, *fields, _id):
        """
        Fetch a person data
        """
        logging.debug("fetch the person data")
        try:
            query_parameter = "/" + _id
            if fields is not None:
                query_parameter += "?fields=" + ",".join(fields)
            print("query parameter: " + query_parameter)

            response = requests.get(self.base_url + '/people' + query_parameter)

            # If the response was successful, no Exception will be raised
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            logging.error('HTTP error occurred: %s', http_err)  # Python 3.6
