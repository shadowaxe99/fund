```python
import unittest
from src.email_sending.email_sender import sendEmail
from src.email_sending.email_tracker import EmailTracker

class TestEmailSending(unittest.TestCase):

    def setUp(self):
        self.emailData = {
            'campaignName': 'Test Campaign',
            'recipients': ['test1@example.com', 'test2@example.com'],
            'template': {
                'subject': 'Test Subject',
                'body': 'Hello, {name}!'
            },
            'attachments': [],
            'schedule': '2022-01-01 00:00:00'
        }
        self.emailTracker = EmailTracker()

    def test_sendEmail(self):
        response = sendEmail(self.emailData)
        self.assertEqual(response['status'], 'success')

    def test_emailTracking(self):
        self.emailTracker.track(self.emailData)
        stats = self.emailTracker.getStats(self.emailData['campaignName'])
        self.assertEqual(stats['sent'], len(self.emailData['recipients']))

if __name__ == '__main__':
    unittest.main()
```