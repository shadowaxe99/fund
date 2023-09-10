```python
import pandas as pd
from src.campaign_creation.contacts_database import ContactsDatabase

class ListHygiene:
    def __init__(self):
        self.contacts_db = ContactsDatabase()

    def update_unsubscribes(self, unsubscribes):
        for email in unsubscribes:
            self.contacts_db.update_contact(email, {"subscribed": False})

    def update_bounces(self, bounces):
        for email in bounces:
            self.contacts_db.update_contact(email, {"valid": False})

    def get_active_contacts(self):
        contacts = self.contacts_db.get_all_contacts()
        active_contacts = [contact for contact in contacts if contact['subscribed'] and contact['valid']]
        return active_contacts

    def get_inactive_contacts(self):
        contacts = self.contacts_db.get_all_contacts()
        inactive_contacts = [contact for contact in contacts if not contact['subscribed'] or not contact['valid']]
        return inactive_contacts

    def get_contact_status(self, email):
        contact = self.contacts_db.get_contact(email)
        if contact:
            return {"subscribed": contact['subscribed'], "valid": contact['valid']}
        else:
            return None

    def export_contact_list(self, filename):
        contacts = self.contacts_db.get_all_contacts()
        df = pd.DataFrame(contacts)
        df.to_csv(filename, index=False)
```