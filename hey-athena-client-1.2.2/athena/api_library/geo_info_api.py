"""

A tool for retrieving geographical info based on external IP
| API Documentation: http://ip-api.com
    
"""

import urllib.request, json

from time import strftime

URL = 'http://ip-api.com/json'
ALIASES = {
    'ip':           'query',
    'latitude':     'lat',
    'longitude':    'lon',
}

response = None

def update_data():
    global response
    response = json.loads(urllib.request.urlopen(URL).read().decode('utf-8'))

def location():
    loc = get_data('city')+', '+get_data('regionName')
    return loc.title()

def time():
    return strftime('%I:%M %p').lstrip('0')
    
def get_data(key):
    """
        Keys/Values:
            | status: SUCCESS,
            | country: COUNTRY,
            | countryCode: COUNTRY CODE,
            | region: REGION CODE,
            | regionName: REGION NAME,
            | city: CITY,
            | zip: ZIP CODE,
            | lat: LATITUDE,
            | lon: LONGITUDE,
            | timezone: TIME ZONE,
            | isp: ISP NAME,
            | org: ORGANIZATION NAME,
            | as: AS NUMBER / NAME,
            | query: IP ADDRESS USED FOR QUERY
    """
    if key in ALIASES:
        key = ALIASES[key]
        
    if 'where' in key.lower() or 'location' in key.lower():
        return location()
    
    if key not in response:
        return None
    return response[key]
