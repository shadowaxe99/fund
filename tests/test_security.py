```python
import unittest
from src.security.compliance import Compliance
from src.security.encryption import Encryption
from src.security.access_controls import AccessControls
from src.security.email_authentication import EmailAuthentication
from src.security.role_based_access import RoleBasedAccess
from src.security.credentials_storage import CredentialsStorage

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.compliance = Compliance()
        self.encryption = Encryption()
        self.access_controls = AccessControls()
        self.email_authentication = EmailAuthentication()
        self.role_based_access = RoleBasedAccess()
        self.credentials_storage = CredentialsStorage()

    def test_compliance(self):
        self.assertTrue(self.compliance.is_compliant())

    def test_encryption(self):
        data = "test data"
        encrypted_data = self.encryption.encrypt(data)
        decrypted_data = self.encryption.decrypt(encrypted_data)
        self.assertEqual(data, decrypted_data)

    def test_access_controls(self):
        self.assertTrue(self.access_controls.check_access("admin"))

    def test_email_authentication(self):
        self.assertTrue(self.email_authentication.authenticate("test@example.com"))

    def test_role_based_access(self):
        self.assertTrue(self.role_based_access.check_access("admin", "campaign_creation"))

    def test_credentials_storage(self):
        credentials = {"username": "test", "password": "password"}
        self.credentials_storage.store(credentials)
        retrieved_credentials = self.credentials_storage.retrieve("username")
        self.assertEqual(credentials, retrieved_credentials)

if __name__ == '__main__':
    unittest.main()
```