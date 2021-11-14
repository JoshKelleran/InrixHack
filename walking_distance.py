from get_user_token import get_creds
from get_geocoordinates import get_goog_API_Key
import requests

def get_walking_directions(parking_lot, final_dest): 
    # parking log is a lat long tuple
    parkingLat, parkingLong = parking_lot[0], parking_lot[1]
    finalLat, finalLong = final_dest[0], final_dest[1]
    API_key = get_goog_API_Key()
    url = f"https://maps.googleapis.com/maps/api/directions/json?destination={finalLat}, {finalLong}origin={finalLat}, {finalLong}&key={API_key}"
    print(url)
    response = requests.get(url)    
    print(response)    
    
get_walking_directions((37.3496418, -121.9389875), (37.3498762, -121.9352013))
