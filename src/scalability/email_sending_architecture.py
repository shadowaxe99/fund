```python
import time
from threading import Thread
from src.email_sending.email_sender import sendEmail
from src.email_sending.email_api import EmailAPI

class EmailSendingArchitecture:
    def __init__(self, email_api: EmailAPI, max_threads: int):
        self.email_api = email_api
        self.max_threads = max_threads

    def send_emails(self, campaignData):
        recipient_list = campaignData['recipients']
        threads = []

        for i in range(0, len(recipient_list), self.max_threads):
            batch = recipient_list[i:i + self.max_threads]
            thread = Thread(target=self._send_email_batch, args=(batch, campaignData,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def _send_email_batch(self, batch, campaignData):
        for recipient in batch:
            emailData = self._prepare_email_data(recipient, campaignData)
            sendEmail(emailData, self.email_api)
            time.sleep(1)  # Throttle to comply with ISP limits

    @staticmethod
    def _prepare_email_data(recipient, campaignData):
        emailData = {
            'to': recipient,
            'subject': campaignData['subject'],
            'body': campaignData['body'].format(recipient=recipient),
            'attachments': campaignData['attachments'],
            'cc': campaignData.get('cc'),
            'bcc': campaignData.get('bcc'),
            'reply_to': campaignData.get('reply_to'),
            'sender': campaignData.get('sender')
        }
        return emailData
```