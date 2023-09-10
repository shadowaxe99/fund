```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailAPI:
    def __init__(self, server, port, username, password):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, emailData):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(emailData['recipients'])
        msg['Subject'] = emailData['subject']

        body = emailData['body']
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(self.server, self.port)
        server.starttls()
        server.login(self.username, self.password)
        text = msg.as_string()
        server.sendmail(self.username, emailData['recipients'], text)
        server.quit()

    def send_bulk_emails(self, campaignData):
        for emailData in campaignData['emails']:
            self.send_email(emailData)
```
