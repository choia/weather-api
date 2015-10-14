import urllib2
import json
import time

api_url = 'http://api.wunderground.com/api/'
api_key = 'bddadf15197d9379'
api_features = '/conditions/q/'
api_location = 'GA/Dunwoody.json'

url = api_url + api_key + api_features + api_location
parsed_url = urllib2.urlopen(url)
json_parsed_url = json.load(parsed_url)
print json_parsed_url['current_observation']['display_location']['full']
print json_parsed_url['current_observation']['weather']
print json_parsed_url['current_observation']['temperature_string']
print json_parsed_url['current_observation']['observation_time']
#convert_time = json_parsed_url['current_observation']['local_epoch']
#print time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(float(convert_time)))
