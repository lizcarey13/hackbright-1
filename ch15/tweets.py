import requests
from requests_oauthlib import OAuth1
import json

from api_keys import *

url = 'https://api.twitter.com/1.1/search/tweets.json'
auth = OAuth1(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                TWITTER_TOKEN, TWITTER_TOKEN_SECRET)

def get_tweets(query_text, count):
    url_query = url + '?q=' + query_text + '&count=' + str(count)
    response = requests.get(url_query, auth=auth)

    tweet_list = []
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        for tweet in data['statuses']:
            tweet_list.append('@' + tweet['user']['screen_name'] + ': ' + tweet['text'])

    return tweet_list

print (get_tweets('hackbright', 10))

