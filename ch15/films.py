from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
api_url = "https://data.sfgov.org/resource/wwmu-gmzc.json"

def get_film_titles_made_in(year):
    api_url_year = api_url + "?release_year=" + str(year)
    response = urlopen(api_url_year)
    json_obj = load(response)

    film_list = []

    for film in json_obj:
        if film["title"] not in film_list:
            film_list.append(film["title"])

    return film_list

print get_film_titles_made_in(2002)