import requests
import datetime


def get_goog_API_Key():
    key = ''
    with open('GOOG_API_KEY.txt', 'r') as f:
        key = f.readline()

    return key


def get_address(lat, lng):
    """
    :return formatted address
    """
    address = ''
    API_KEY = get_goog_API_Key()
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={API_KEY}"

    response = requests.get(url)
    # try catch for empty query result
    results = response.json()['results'][0]

    add_components = results['address_components']

    for x in range(7):
        if add_components[x]['long_name']:
            if x > 0:
                address = address + ', ' + add_components[x]['long_name']
            else:
                address = add_components[x]['long_name']
    return address

