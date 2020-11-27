"""
Services tests
"""
from ghibli.services.composite_service import CompositeService
from ghibli.services.movie_service import MovieService
from ghibli.services.person_service import PersonService

def test_composite_service():
    """
    Test composite service
    """
    service_composite = CompositeService()
    movies = service_composite.fetch_all_movies()
    assert movies is not None
    assert len(movies) > 0

def test_movie_service():
    """
    Test movie service
    """
    service_movie = MovieService()
    movies = service_movie.fetch_all_movies('id', limit=1)
    assert movies is not None
    # check if the service fetched only one movie record
    assert len(movies) == 1
    assert 'id' in movies[0]
    assert movies[0]['id'] is not None

def test_person_service():
    """
    Test person service
    """
    service_person = PersonService()
    people = service_person.fetch_all_people('id', limit=1)
    assert people is not None
    # check if the service fetched only one people record
    assert len(people) == 1
    assert 'id' in people[0]
    assert people[0]['id'] is not None
