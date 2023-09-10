```python
import logging
from src.security.role_based_access import RoleBasedAccessControl

class AccessControls:
    def __init__(self):
        self.rbac = RoleBasedAccessControl()
        self.logger = logging.getLogger(__name__)

    def check_access(self, user, resource):
        role = user.get_role()
        if self.rbac.has_access(role, resource):
            self.logger.info(f"Access granted for {user.get_username()} to {resource}")
            return True
        else:
            self.logger.warning(f"Access denied for {user.get_username()} to {resource}")
            return False

    def log_activity(self, user, action):
        self.logger.info(f"{user.get_username()} performed {action}")

    def update_security_settings(self, securityData):
        self.rbac.update_roles(securityData.get('roles'))
        self.logger.info("Security settings updated")
```