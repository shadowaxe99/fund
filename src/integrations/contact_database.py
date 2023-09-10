```python
import os
from salesforce_bulk import SalesforceBulk
from salesforce_bulk.util import IteratorBytesIO
import csv
import json

class ContactDatabase:
    def __init__(self):
        self.bulk = SalesforceBulk(username=os.getenv('SALESFORCE_USERNAME'), password=os.getenv('SALESFORCE_PASSWORD'), security_token=os.getenv('SALESFORCE_SECURITY_TOKEN'))

    def get_contacts(self, campaignData):
        job = self.bulk.create_query_job("Contact", contentType='CSV')
        batch = self.bulk.query(job, "select Id, Email, FirstName, LastName from Contact")
        self.bulk.close_job(job)
        while not self.bulk.is_batch_done(batch):
            pass
        for result in self.bulk.get_all_results_for_query_batch(batch):
            reader = csv.DictReader(IteratorBytesIO(result), delimiter=',')
            for row in reader:
                campaignData['recipients'].append({'id': row['Id'], 'email': row['Email'], 'firstName': row['FirstName'], 'lastName': row['LastName']})
        return campaignData

    def update_contact(self, contactId, responseData):
        job = self.bulk.create_upsert_job("Contact", contentType='CSV')
        csv_iter = IteratorBytesIO(self._create_csv_content(responseData).encode('utf-8'))
        batch = self.bulk.post_batch(job, csv_iter)
        self.bulk.wait_for_batch(job, batch)
        self.bulk.close_job(job)

    def _create_csv_content(self, responseData):
        csv_data = "Id,Response\n"
        for response in responseData:
            csv_data += "{},{}\n".format(response['contactId'], response['response'])
        return csv_data
```