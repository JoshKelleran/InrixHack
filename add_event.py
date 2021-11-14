from googleapiclient.discovery import build
from get_user_token import get_creds

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
        parking_message = 'very high'

    event = {
        'summary': "Driving to " + event_name,
        'description': f'You have a {parking_message} probability of finding parking near your event\n https://www.google.com/maps/dir/{start_location[0]},{start_location[1]}/{end_location[0]},{end_location[1]}',
        'start': {
            'dateTime': start,
        },
        'colorId': 5,
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

