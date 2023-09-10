```python
import requests
from src.security.credentials_storage import get_credentials

class EmailAPI:
    def __init__(self):
        self.credentials = get_credentials('email_api')

    def send_email(self, emailData):
        if self.credentials['provider'] == 'SendGrid':
            self.send_via_sendgrid(emailData)
        elif self.credentials['provider'] == 'Mailgun':
            self.send_via_mailgun(emailData)
        elif self.credentials['provider'] == 'Mailchimp':
            self.send_via_mailchimp(emailData)
        elif self.credentials['provider'] == 'AmazonSES':
            self.send_via_amazon_ses(emailData)
        else:
            raise Exception('Unsupported email provider')

    def send_via_sendgrid(self, emailData):
        headers = {
            'Authorization': 'Bearer ' + self.credentials['api_key'],
            'Content-Type': 'application/json'
        }
        data = {
            'personalizations': [{
                'to': [{'email': recipient} for recipient in emailData['recipients']],
                'subject': emailData['subject']
            }],
            'from': {'email': self.credentials['sender_email']},
            'content': [{'type': 'text/plain', 'value': emailData['body']}]
        }
        response = requests.post('https://api.sendgrid.com/v3/mail/send', headers=headers, json=data)
        response.raise_for_status()

    def send_via_mailgun(self, emailData):
        data = {
            'from': self.credentials['sender_email'],
            'to': emailData['recipients'],
            'subject': emailData['subject'],
            'text': emailData['body']
        }
        response = requests.post('https://api.mailgun.net/v3/' + self.credentials['domain'] + '/messages', auth=('api', self.credentials['api_key']), data=data)
        response.raise_for_status()

    def send_via_mailchimp(self, emailData):
        # Implementation for Mailchimp goes here
        pass

    def send_via_amazon_ses(self, emailData):
        # Implementation for Amazon SES goes here
        pass
```