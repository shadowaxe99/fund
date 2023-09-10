```python
import tableau_api_lib
from tableau_api_lib import TableauServerConnection
from looker_sdk import client, models
import powerbi
from powerbi.session import PowerBISession

class BIToolsIntegration:
    def __init__(self, integrationData):
        self.integrationData = integrationData

    def connect_tableau(self):
        tableau_auth = tableau_api_lib.TableauAuth(
            self.integrationData['tableau']['username'],
            self.integrationData['tableau']['password'],
            self.integrationData['tableau']['site_id']
        )
        self.tableau_server = TableauServerConnection(tableau_auth)
        self.tableau_server.sign_in()

    def connect_looker(self):
        self.looker_client = client.setup("looker.ini")

    def connect_powerbi(self):
        self.powerbi_session = PowerBISession(
            self.integrationData['powerbi']['tenant'],
            self.integrationData['powerbi']['client_id'],
            self.integrationData['powerbi']['client_secret']
        )

    def update_integration(self, new_integrationData):
        self.integrationData = new_integrationData

    def get_tableau_reports(self):
        return self.tableau_server.get_published_data_sources()

    def get_looker_reports(self):
        return self.looker_client.all_looks()

    def get_powerbi_reports(self):
        return self.powerbi_session.get_reports()

    def close_connections(self):
        self.tableau_server.sign_out()
        self.looker_client.logout()
        self.powerbi_session.logout()
```