```python
import json
from src.integrations.email_api import EmailAPI

class EmailTracker:
    def __init__(self):
        self.email_api = EmailAPI()
        self.tracking_data = {
            'opens': 0,
            'clicks': 0,
            'unsubscribes': 0,
            'bounces': 0
        }

    def track_email(self, email_id):
        tracking_info = self.email_api.get_tracking_info(email_id)
        self.update_tracking_data(tracking_info)

    def update_tracking_data(self, tracking_info):
        self.tracking_data['opens'] += tracking_info['opens']
        self.tracking_data['clicks'] += tracking_info['clicks']
        self.tracking_data['unsubscribes'] += tracking_info['unsubscribes']
        self.tracking_data['bounces'] += tracking_info['bounces']

    def get_tracking_data(self):
        return self.tracking_data

    def reset_tracking_data(self):
        self.tracking_data = {
            'opens': 0,
            'clicks': 0,
            'unsubscribes': 0,
            'bounces': 0
        }
```