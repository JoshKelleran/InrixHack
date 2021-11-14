import requests

def format_address_string(raw_string):
    word_list = raw_string.replace(' ', '+')
    return word_list


def get_goog_API_Key():
    key = ''
    with open('GOOG_API_KEY.txt', 'r') as f:
        key = f.readline()

    return key

def get_lat_long(raw_string):

    """
    :return tuple (lat, long)
    """
    address = format_address_string(raw_string)
    API_KEY = get_goog_API_Key()
    url="https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (address, API_KEY)

    response = requests.get(url)

    # try catch for empty query result
    results = response.json()['results'][0]

    lat = results['geometry']['location']['lat']
    long = results['geometry']['location']['lng']

    return lat, long


