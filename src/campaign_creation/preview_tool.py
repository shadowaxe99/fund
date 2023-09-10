```python
from campaign import Campaign
from email_sender import EmailSender

class PreviewTool:
    def __init__(self):
        self.campaign = Campaign()
        self.email_sender = EmailSender()

    def preview_campaign(self, campaignData):
        """
        This function previews the campaign by sending a test email to the user.
        """
        # Validate the campaign data
        if not self.campaign.validate_campaign_data(campaignData):
            return "Invalid campaign data"

        # Create a test email
        emailData = {
            "subject": campaignData["email_template"]["subject"],
            "body": campaignData["email_template"]["body"],
            "recipients": [campaignData["creator"]],
            "attachments": campaignData["attachments"],
            "sender": campaignData["creator"]
        }

        # Send the test email
        if not self.email_sender.send_email(emailData):
            return "Failed to send test email"

        return "Test email sent successfully"

    def preview_template(self, template):
        """
        This function previews the template by rendering it with dummy data.
        """
        # Validate the template
        if not self.campaign.validate_template(template):
            return "Invalid template"

        # Render the template with dummy data
        rendered_template = self.campaign.render_template(template, {"name": "Test User"})

        return rendered_template
```