```python
import datetime

class Calendar:
    def __init__(self):
        self.schedule = {}

    def add_schedule(self, campaign_id, send_date_time):
        if not isinstance(send_date_time, datetime.datetime):
            raise ValueError("send_date_time must be a datetime object")
        self.schedule[campaign_id] = send_date_time

    def remove_schedule(self, campaign_id):
        if campaign_id in self.schedule:
            del self.schedule[campaign_id]

    def get_schedule(self, campaign_id):
        return self.schedule.get(campaign_id, None)

    def get_all_schedules(self):
        return self.schedule
```