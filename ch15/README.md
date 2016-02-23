# API Code Samples

## Installation
- In order to run the code samples that need API key, you will need to obtain valid API key:
  - [`films.py`](films.py) - This uses [SF Open Data on Film Locations](https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am), and no API key is required.
  - [`weather.py`](weather.py) - This uses [WeatherUnderground API](https://www.wunderground.com/weather/api). An API key is needed before continuing.
  - [`tweets.py`](tweets.py) - This use [Twitter API](https://dev.twitter.com/rest/public). API key, API secret key, token, and secret token is needed before continuing.

- Copy [`api_keys.py.template`](api_keys.py.template) to a new file called `api_keys.py` in the current directory
- Replace your API keys in `api_keys.py`
  - PLEASE REMEMBER TO NEVER COMMIT YOUR API KEYS TO GITHUB
  - Do a `git status` before you `git add`, and make sure `api_keys.py` doesn't appear as a tracked file 
- [`.gitignore`](.gitignore) file will keep track of which files you do not want git to ever track

- You will also need to install external modules to run `tweets.py`, run the following in your terminal:
  ```shell
  pip install -r requirements.txt
  ```
- If you do not have `pip` yet, follow instructions [here](https://pip.pypa.io/en/stable/installing/) to install `pip`.



