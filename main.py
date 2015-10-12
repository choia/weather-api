import urllib2
import json

api_url = 'http://api.wunderground.com/api/'
api_key = 'bddadf15197d9379'
api_features = '/geolookup/conditions/q/'
api_location = 'GA/Dunwoody.json'

url = api_url + api_key + api_features + api_location
parsed_url = urllib2.urlopen(url)
json_parsed_url = json.load(parsed_url)
print json_parsed_url
