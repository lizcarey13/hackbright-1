import urllib2
import json
from api_keys import *

url_base = 'http://api.wunderground.com/api/' + WEATHER_KEY

def get_temp_in(city, state_abbrev):
    f = urllib2.urlopen(url_base + '/geolookup/conditions/q/'+ state_abbrev + '/' + city + '.json')
    print f
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    temp_f = parsed_json['current_observation']['temp_f']
    return temp_f
    f.close()


print "Current temperature in %s is: %s" % ('San Francisco', get_temp_in('San_Francisco', 'CA'))
