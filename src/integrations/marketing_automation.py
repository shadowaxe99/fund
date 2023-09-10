```python
import requests
from src.shared import integrationData

class MarketingAutomation:
    def __init__(self):
        self.api_key = integrationData['marketing_automation']['api_key']
        self.base_url = integrationData['marketing_automation']['base_url']

    def create_campaign(self, campaignData):
        url = f"{self.base_url}/campaigns"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'name': campaignData['name'],
            'recipients': campaignData['recipients'],
            'template': campaignData['template'],
            'schedule': campaignData['schedule']
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print('Campaign created successfully')
        else:
            print('Failed to create campaign')

    def send_email(self, emailData):
        url = f"{self.base_url}/emails"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'campaign_id': emailData['campaign_id'],
            'recipient': emailData['recipient'],
            'subject': emailData['subject'],
            'body': emailData['body']
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print('Email sent successfully')
        else:
            print('Failed to send email')

    def analyze_response(self, responseData):
        url = f"{self.base_url}/responses"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'campaign_id': responseData['campaign_id'],
            'response': responseData['response']
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print('Response analyzed successfully')
        else:
            print('Failed to analyze response')
```