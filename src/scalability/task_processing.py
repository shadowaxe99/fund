```python
from celery import Celery
from src.email_sending.email_sender import sendEmail
from src.response_handling.response_analyzer import handleResponse

# Initialize Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_email_task(campaignData, emailData):
    """
    Asynchronous task for sending emails.
    """
    sendEmail(campaignData, emailData)

@app.task
def handle_response_task(responseData):
    """
    Asynchronous task for handling responses.
    """
    handleResponse(responseData)
```