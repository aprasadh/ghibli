"""
Movie Service module
"""
import logging
from ghibli.services.movie_service import MovieService
from ghibli.services.person_service import PersonService
from ghibli.config_parser import config_parser


class CompositeService:
    """
    A composite service of movie and person services
    """
    base_url = config_parser['Default']['BaseUrl']

    def fetch_all_movies(self):
        """
        Fetching all movies from composite service
        """
        logging.debug("Fetching all movies from composite service")
        service_movie = MovieService()
        service_person = PersonService()
        # Fetch all movies
        movies = service_movie.fetch_all_movies('id', 'title')
        movie_dict = {}
        for movie in movies:
            movie_dict[movie['id']] = movie
        # Fetch all people
        people = service_person.fetch_all_people('id', 'name', 'films')
        url_length = len(self.base_url + '/films/')
        # Merge people data with movies
        for person in people:
            for _id in person['films']:
                movie = movie_dict[_id[url_length:]]
                if 'people' in movie:
                    movie['people'].append(person)
                else:
                    movie['people'] = []
                    movie['people'].append(person)
        return movies
