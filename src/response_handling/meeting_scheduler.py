```python
import datetime
from src.integrations.calendar import CalendarAPI

class MeetingScheduler:
    def __init__(self):
        self.calendar_api = CalendarAPI()

    def schedule_meeting(self, responseData):
        if 'meeting_request' in responseData:
            meeting_info = responseData['meeting_request']
            start_time = datetime.datetime.strptime(meeting_info['start_time'], '%Y-%m-%dT%H:%M:%S')
            end_time = datetime.datetime.strptime(meeting_info['end_time'], '%Y-%m-%dT%H:%M:%S')
            attendees = meeting_info['attendees']
            subject = meeting_info['subject']

            self.calendar_api.create_event(start_time, end_time, attendees, subject)
```