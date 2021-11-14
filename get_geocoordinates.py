import requests

lat, long = None, None
raw_loc = '3355 Brookdale Drive, Santa Clara, CA'

def format_address_string(raw_string):

    word_list = raw_string.replace(' ', '+')
    return word_list


def get_goog_API_Key():
    key = ''
    with open('GOOG_API_KEY.txt', 'r') as f:
        key = f.readline()

    return key

def get_lat_long(address):
    """
    :return tuple (lat, long)
    """
    API_KEY = get_goog_API_Key()
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, API_KEY)

    response = requests.get(url)
    print(url)
    print(response)

    results = response.json()['results'][0]

    lat = results['geometry']['location']['lat']
    long = results['geometry']['location']['lng']

    return lat, long


