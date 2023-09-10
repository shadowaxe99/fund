```python
from enum import Enum
from typing import Dict

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

class User:
    def __init__(self, user_id: str, role: Role):
        self.user_id = user_id
        self.role = role

class RoleBasedAccessControl:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def add_user(self, user_id: str, role: Role):
        if user_id in self.users:
            raise Exception("User already exists")
        self.users[user_id] = User(user_id, role)

    def remove_user(self, user_id: str):
        if user_id not in self.users:
            raise Exception("User does not exist")
        del self.users[user_id]

    def change_role(self, user_id: str, new_role: Role):
        if user_id not in self.users:
            raise Exception("User does not exist")
        self.users[user_id].role = new_role

    def can_edit(self, user_id: str):
        if user_id not in self.users:
            raise Exception("User does not exist")
        return self.users[user_id].role in [Role.ADMIN, Role.EDITOR]

    def can_view(self, user_id: str):
        if user_id not in self.users:
            raise Exception("User does not exist")
        return self.users[user_id].role in [Role.ADMIN, Role.EDITOR, Role.VIEWER]
```