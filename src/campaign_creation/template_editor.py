```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader

class TemplateEditor:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('templates'))

    def create_template(self, template_name, subject, body):
        template = self.env.get_template(template_name)
        return template.render(subject=subject, body=body)

    def save_template(self, template_name, subject, body):
        with open(f'templates/{template_name}.html', 'w') as file:
            file.write(self.create_template(template_name, subject, body))

    def load_template(self, template_name):
        with open(f'templates/{template_name}.html', 'r') as file:
            return file.read()

    def create_email(self, template_name, recipient, merge_fields):
        template = self.load_template(template_name)
        email = MIMEMultipart()
        email['From'] = 'noreply@ourapp.com'
        email['To'] = recipient
        email['Subject'] = template.subject
        body = template.body.format(**merge_fields)
        email.attach(MIMEText(body, 'html'))
        return email.as_string()
```