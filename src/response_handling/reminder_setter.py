```python
import datetime
from src.integrations.calendar import CalendarIntegration

class ReminderSetter:
    def __init__(self):
        self.calendar = CalendarIntegration()

    def set_reminder(self, responseData):
        if 'follow_up' in responseData and responseData['follow_up']:
            reminder_time = self.calculate_reminder_time(responseData['received_time'])
            self.calendar.create_event(reminder_time, "Follow up on email response")

    def calculate_reminder_time(self, received_time):
        # Set reminder for 24 hours after response received
        return received_time + datetime.timedelta(days=1)
```