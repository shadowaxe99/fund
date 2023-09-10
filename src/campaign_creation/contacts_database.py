```python
import sqlite3
from sqlite3 import Error

class ContactsDatabase:
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def create_table(self):
        try:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                );
            """)
        except Error as e:
            print(e)

    def add_contact(self, name, email):
        try:
            self.conn.execute("""
                INSERT INTO contacts(name, email)
                VALUES (?, ?);
            """, (name, email))
            self.conn.commit()
        except Error as e:
            print(e)

    def get_all_contacts(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM contacts")
        return cur.fetchall()

    def get_contact_by_email(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM contacts WHERE email=?", (email,))
        return cur.fetchone()

    def delete_contact(self, email):
        try:
            self.conn.execute("""
                DELETE FROM contacts WHERE email=?;
            """, (email,))
            self.conn.commit()
        except Error as e:
            print(e)

    def update_contact(self, name, email):
        try:
            self.conn.execute("""
                UPDATE contacts
                SET name = ?
                WHERE email = ?;
            """, (name, email))
            self.conn.commit()
        except Error as e:
            print(e)
```