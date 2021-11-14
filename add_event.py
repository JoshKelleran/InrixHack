from googleapiclient.discovery import build
from get_user_token import get_creds


def set_events(event_name, location, start, end, prob_of_parking):

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
        'summary': event_name,
        'location': location,
        'description': f'You have a {parking_message} probability of finding parking near your event',
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


set_events('Go To School', 'Santa Clara', "12:00", '1:00', 2)