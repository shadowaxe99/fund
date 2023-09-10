```python
from datetime import datetime
from typing import List, Dict

class Campaign:
    def __init__(self, name: str, recipients: List[str], template: Dict, attachments: List[str], schedule: datetime):
        self.name = name
        self.recipients = recipients
        self.template = template
        self.attachments = attachments
        self.schedule = schedule

    def create_campaign(self):
        campaignData = {
            'name': self.name,
            'recipients': self.recipients,
            'template': self.template,
            'attachments': self.attachments,
            'schedule': self.schedule
        }
        return campaignData

    def preview_campaign(self, campaignData):
        print(f"Campaign Name: {campaignData['name']}")
        print(f"Recipients: {', '.join(campaignData['recipients'])}")
        print(f"Email Subject: {campaignData['template']['subject']}")
        print(f"Email Body: {campaignData['template']['body']}")
        print(f"Attachments: {', '.join(campaignData['attachments'])}")
        print(f"Scheduled for: {campaignData['schedule']}")

    def save_campaign(self, campaignData):
        # Save the campaign data to a database or file
        pass
```