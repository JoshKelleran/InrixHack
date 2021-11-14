import datetime
from googleapiclient.discovery import build
from get_user_token import get_creds
from get_geocoordinates import get_lat_long
import pytz

def get_events():

    creds = get_creds()
    event_data = []

    service = build('calendar', 'v3', credentials=creds)

    # Future functionality:

    # Call the Calendar API
    now_time = datetime.datetime.utcnow()
    now_offset = pytz.utc.localize(now_time)        # Making timezone aware to enable time delta
    now = now_time.isoformat() + 'Z'  # 'Z' indicates UTC time
    
    # print("Getting Next Week's worth of data")
   
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=672, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    #if not events:
    #    print('No upcoming events found.')
    for event in events:
        start_string = event['start'].get('dateTime', event['start'].get('date'))
        if not 'T' in start_string: # no time (only date) for event
            continue
        start_time = datetime.datetime.strptime(start_string, "%Y-%m-%dT%H:%M:%S%z")
        if start_time - now_offset > datetime.timedelta(days=7): # TODO: Filter out invalid Locations
            break
        if 'location' in event.keys():
            lat_long = get_lat_long(event['location'])
            event_data.append((event["summary"], start_time, lat_long))

    #print(event_data)
    return event_data


