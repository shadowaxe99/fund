```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.email_sending.email_api import EmailAPI
from src.campaign_creation.campaign import CampaignSchema

class EmailSender:
    def __init__(self, server="localhost"):
        self.server = server
        self.email_api = EmailAPI()

    def send_email(self, campaignData):
        campaign = CampaignSchema().load(campaignData)
        msg = MIMEMultipart()
        msg['From'] = campaign.sender
        msg['To'] = ', '.join(campaign.recipients)
        msg['Subject'] = campaign.subject
        msg.attach(MIMEText(campaign.body, 'plain'))

        try:
            server = smtplib.SMTP(self.server)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")

    def send_campaign_emails(self, campaignData):
        for emailData in campaignData['emails']:
            self.send_email(emailData)

    def throttle_emails(self, campaignData, limit):
        emails_sent = 0
        for emailData in campaignData['emails']:
            if emails_sent < limit:
                self.send_email(emailData)
                emails_sent += 1
            else:
                break
```