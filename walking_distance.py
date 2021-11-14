import datetime
from get_user_token import get_creds
from get_geocoordinates import get_goog_API_Key
import requests
import pytz
from pprint import pprint
from get_calendar_events import get_events

def get_walking_time(start_time_string, parking_lot, final_dest):
    # parkinglot  is a lat long tuple
    parkingLat, parkingLong = parking_lot[0], parking_lot[1]
    finalLat, finalLong = final_dest[0], final_dest[1]
    API_key = get_goog_API_Key()
    start_time = datetime.datetime.strptime(start_time_string, "%Y-%m-%dT%H:%M:%S%z")

    arrival_time = (start_time - pytz.utc.localize(datetime.datetime(1970,1,1))).total_seconds()

    url = f"https://maps.googleapis.com/maps/api/directions/json?destination={finalLat}, {finalLong}&origin={parkingLat}, {parkingLong}&arrival_time={arrival_time}&mode=walking&key={API_key}"

    response = requests.get(url) 

    results = response.json()   
    return int(results['routes'][0]['legs'][0]['duration']['text'].split()[0])# returns walking time

#print(get_events())
#get_walking_directions(datetime.datetime.now(), (37.32362, -121.972528), (37.3498762, -121.9352013))
