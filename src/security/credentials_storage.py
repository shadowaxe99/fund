```python
import os
from cryptography.fernet import Fernet

class CredentialStorage:
    def __init__(self):
        self.key = os.getenv('SECRET_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_credentials(self, credentials):
        encrypted_credentials = self.cipher_suite.encrypt(credentials.encode())
        return encrypted_credentials

    def decrypt_credentials(self, encrypted_credentials):
        decrypted_credentials = self.cipher_suite.decrypt(encrypted_credentials).decode()
        return decrypted_credentials

    def store_credentials(self, service_name, credentials):
        encrypted_credentials = self.encrypt_credentials(credentials)
        with open(f"{service_name}_credentials.txt", "wb") as file:
            file.write(encrypted_credentials)

    def retrieve_credentials(self, service_name):
        with open(f"{service_name}_credentials.txt", "rb") as file:
            encrypted_credentials = file.read()
        return self.decrypt_credentials(encrypted_credentials)
```