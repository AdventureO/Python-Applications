"""
    geolocator.py
    A simple IP geolocation python script.
    Uses freegeoip.net geolocation web service.
    Requires requests, json and sys libraries.

    Example:
    $ ./geolocator.py 198.117.0.122

    IP : 198.117.0.122
    Country code: US
    Country : United States
    Region code: AL
    Region: Alabama
    City : Huntsville
    Zip code : 35812
    Time zone : America/Chicago
    Latitude : 34.7304
    Longitude : -86.5861
    Metro code : 691
"""

import json
import requests
import sys

def get_location(ip_address):

    # url which loads json page with info about location
    url = 'http://freegeoip.net/json/' + ip_address

    # get json data from page with info about location
    r = requests.get(url)

    # parsing data and decode it
    data = json.loads(r.content.decode('utf-8'))

    # load data from json type structure to simple variables
    ip = data['ip']
    country_code = data['country_code']
    country = data['country_name']
    region_code = data['region_code']
    region_name = data['region_name']
    city = data['city']
    zip_code = data['zip_code']
    time_zone = data['time_zone']
    latitude = data['latitude']
    longitude = data['longitude']
    metro_code = data['metro_code']

    # print all data about location
    print('IP : {0} \nCountry code: {1} \nCountry : {2} \nRegion code: {3} \nRegion: {4} '
          '\nCity : {5} \nZip code : {6} \nTime zone : {7} \nLatitude : {8} \nLongitude : {9} \nMetro code : {10}'
          .format( ip, country_code, country, region_code, region_name,
                   city, zip_code, time_zone, latitude, longitude, metro_code))

#get_location('198.117.0.122')

# Check if you enter an argument
if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_location(sys.argv[1])
    else:
        get_location('127.0.0.1')