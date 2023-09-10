```python
import os
from crm_sdk import CRM

class CRMSytem:
    def __init__(self):
        self.crm = CRM(os.getenv('CRM_API_KEY'))

    def enter_lead(self, responseData):
        if responseData.get('lead_detected'):
            lead_info = {
                'name': responseData.get('name'),
                'email': responseData.get('email'),
                'phone': responseData.get('phone'),
                'company': responseData.get('company'),
                'source': 'Email Campaign',
                'notes': responseData.get('response_text')
            }
            self.crm.create_lead(lead_info)

    def update_lead(self, responseData):
        if responseData.get('lead_detected'):
            lead_info = {
                'name': responseData.get('name'),
                'email': responseData.get('email'),
                'phone': responseData.get('phone'),
                'company': responseData.get('company'),
                'source': 'Email Campaign',
                'notes': responseData.get('response_text')
            }
            self.crm.update_lead(lead_info)

    def handle_response(self, responseData):
        if responseData.get('lead_detected'):
            if self.crm.lead_exists(responseData.get('email')):
                self.update_lead(responseData)
            else:
                self.enter_lead(responseData)
```