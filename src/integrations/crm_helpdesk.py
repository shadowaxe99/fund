```python
import requests
from src.shared_dependencies import integrationData, ResponseSchema

class CRMHelpdeskIntegration:
    def __init__(self):
        self.crm_url = integrationData['crm_helpdesk']['url']
        self.api_key = integrationData['crm_helpdesk']['api_key']

    def enter_into_crm(self, response):
        """
        Enter the response into the CRM system if a lead is detected.
        """
        if ResponseSchema(response).is_lead:
            payload = {
                'lead_info': response,
                'api_key': self.api_key
            }
            response = requests.post(self.crm_url, data=payload)
            if response.status_code == 200:
                print("Lead entered into CRM system successfully.")
            else:
                print("Failed to enter lead into CRM system.")

    def route_to_team_member(self, response):
        """
        Route the response to the right team member if follow-up is needed.
        """
        if ResponseSchema(response).needs_follow_up:
            payload = {
                'response_info': response,
                'api_key': self.api_key
            }
            response = requests.post(self.crm_url, data=payload)
            if response.status_code == 200:
                print("Response routed to team member successfully.")
            else:
                print("Failed to route response to team member.")
```