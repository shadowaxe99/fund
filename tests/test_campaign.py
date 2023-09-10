```python
import unittest
from src.campaign_creation.campaign import Campaign
from src.campaign_creation.contacts_database import ContactsDatabase
from src.campaign_creation.template_editor import TemplateEditor
from src.campaign_creation.file_uploader import FileUploader
from src.campaign_creation.calendar import Calendar
from src.campaign_creation.preview_tool import PreviewTool

class TestCampaign(unittest.TestCase):

    def setUp(self):
        self.campaign = Campaign()
        self.contacts_db = ContactsDatabase()
        self.template_editor = TemplateEditor()
        self.file_uploader = FileUploader()
        self.calendar = Calendar()
        self.preview_tool = PreviewTool()

    def test_create_campaign(self):
        campaign_data = {
            'name': 'Test Campaign',
            'recipients': ['test1@example.com', 'test2@example.com'],
            'template': {
                'subject': 'Test Subject',
                'body': 'Hello, {name}!'
            },
            'attachments': ['file1.pdf', 'file2.jpg'],
            'schedule': '2022-01-01 00:00:00'
        }
        self.campaign.create(campaign_data)
        self.assertEqual(self.campaign.data, campaign_data)

    def test_select_recipients(self):
        self.contacts_db.select(['test1@example.com', 'test2@example.com'])
        self.assertEqual(self.contacts_db.selected, ['test1@example.com', 'test2@example.com'])

    def test_edit_template(self):
        template_data = {
            'subject': 'Test Subject',
            'body': 'Hello, {name}!'
        }
        self.template_editor.edit(template_data)
        self.assertEqual(self.template_editor.data, template_data)

    def test_upload_files(self):
        self.file_uploader.upload(['file1.pdf', 'file2.jpg'])
        self.assertEqual(self.file_uploader.files, ['file1.pdf', 'file2.jpg'])

    def test_select_schedule(self):
        self.calendar.select('2022-01-01 00:00:00')
        self.assertEqual(self.calendar.selected, '2022-01-01 00:00:00')

    def test_preview_campaign(self):
        campaign_data = {
            'name': 'Test Campaign',
            'recipients': ['test1@example.com', 'test2@example.com'],
            'template': {
                'subject': 'Test Subject',
                'body': 'Hello, {name}!'
            },
            'attachments': ['file1.pdf', 'file2.jpg'],
            'schedule': '2022-01-01 00:00:00'
        }
        self.preview_tool.preview(campaign_data)
        self.assertEqual(self.preview_tool.previewed, campaign_data)

if __name__ == '__main__':
    unittest.main()
```