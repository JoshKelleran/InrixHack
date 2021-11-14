import datetime
from get_user_token import get_creds
from get_geocoordinates import get_goog_API_Key
import requests
from pprint import pprint
from get_calendar_events import get_events

def get_walking_directions(start_time, parking_lot, final_dest): 
    # parkinglot  is a lat long tuple
    parkingLat, parkingLong = parking_lot[0], parking_lot[1]
    finalLat, finalLong = final_dest[0], final_dest[1]
    API_key = get_goog_API_Key()
    arrival_time = (start_time-datetime.datetime(1970,1,1)).total_seconds()
    #print(arrival_time)
    url = f"https://maps.googleapis.com/maps/api/directions/json?destination={finalLat}, {finalLong}&origin={parkingLat}, {parkingLong}&arrival_time={arrival_time}&mode=walking&key={API_key}"
    #print(url)
    response = requests.get(url) 
    #print(response)
    results = response.json()   
    return results['routes'][0]['legs'][0]['duration']['text'] # returns walking time    

#print(get_events())
#get_walking_directions(datetime.datetime.now(), (37.32362, -121.972528), (37.3498762, -121.9352013))
