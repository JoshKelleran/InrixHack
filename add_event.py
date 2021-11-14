from googleapiclient.discovery import build
from get_user_token import get_creds
import datetime

def set_events(event_name, start_location, end_location, start, end, prob_of_parking):

    creds = get_creds()
    service = build('calendar', 'v3', credentials=creds)
    parking_message = ''

    if prob_of_parking == 1:
        parking_message = 'very low'
    elif prob_of_parking == 2:
        parking_message = 'low'
    elif prob_of_parking == 3:
        parking_message = 'medium'
    elif prob_of_parking == 4:
        parking_message = 'high'
    elif prob_of_parking == 5:
        parking_message = 'very high'z

    event = {
        'summary': "Driving to" + event_name,
        'location': 
        'description': f'You have a {parking_message} probability of finding parking near your event\n'+"https://www.google.com/maps/dir/"+start_location[0]+','+start_location[1]+'/'+end_location[0]+
        ','+end_location[1])
        'start': {
            'dateTime': start,
        },
        'end': {
            'dateTime': end,
        },
        'recurrence': [

        ],
        'attendees': [

        ],
        'reminders': {
            'useDefault': False,
            'overrides': [

            ],
        },
    }

    # add try catch
    event = service.events().insert(calendarId='primary', body=event).execute()
    
if __name__ == "__main__":
    set_events("Inrix Hack Presentations", (37.3496418, -121.9389875), (37.3498762, -121.9352013), datetime.datetime.now(), datetime.datetime.now()+ datetime1
