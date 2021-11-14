import datetime
from googleapiclient.discovery import build
from get_user_token import get_creds


def get_events():

    creds = get_creds()
    event_data = []

    service = build('calendar', 'v3', credentials=creds)

    # Future functionality:

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=168, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))

        if 'location' in event.keys():
            print(start)

            event_data.append((event['summary'], start, event['location']))


