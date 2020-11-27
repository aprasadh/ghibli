# Ghibli Assignment Notes

* The application is developed and tested with Python 3.9, but should also work in v3.8
* All the dependent packages are listed in `requirements.txt`
* `pylint` is used to ensure the code is written according to PEP8 style guidelines. A generated `.pylintrc` is provided in the root folder.
* As per the requirement, I didn't access the third party API for every call. So, I enabled time bound caching using a third party library called `cachetools`. This demonstrates caching. Since `cachetools` uses in-process caching, in production it is not suitable, hence a dedicated caching server using `memcache` or `redis` can be deployed.
* Test cases are written using `pytest`. I tried my best to cover all test cases except the cache hit/miss scenario. This may tested by instrumenting and monitoring the caching servers.

## Setup

I used Mac environment for development.

* Go to the project directory in the terminal.
* Create a virtual environment by running,
  * `python -m venv myenv`
* Activate the virtual environment
  * `source myenv/bin/activate`
* Install the project dependencies
  * `pip install -r requirements.txt`
* Run the server,
  * `uvicorn --log-level debug ghibli.main:app --reload`
* Open the link `http://localhost:8000/movies` using browser. It displays the movie list page

To run test cases, please run `pytest` command from the project root folder.
