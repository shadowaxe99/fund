```python
import dkim
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailAuthenticator:
    def __init__(self, private_key, domain, selector):
        self.private_key = private_key
        self.domain = domain
        self.selector = selector

    def sign_email(self, subject, body, sender, recipient):
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = sender
        message['To'] = recipient
        message.attach(MIMEText(body, 'plain'))

        headers = ['To', 'From', 'Subject']
        sig = dkim.sign(message.as_string(), self.selector, self.domain, self.private_key, include_headers=headers)
        sig = sig.decode()

        message['DKIM-Signature'] = sig[len('DKIM-Signature: '):]

        return message.as_string()

    def send_email(self, server, port, username, password, message):
        with smtplib.SMTP(server, port) as smtp:
            smtp.login(username, password)
            smtp.sendmail(message['From'], message['To'], message.as_string())
```
