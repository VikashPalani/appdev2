#import libraries

import yagmail
from celery import Celery
from datetime import timedelta
import redis
from celery.schedules import crontab

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
email_address = '22f3001758@ds.study.iitm.ac.in'
app_password = 'onypwhekxiwluepa'

pdf_path = 'MonthlyReport.pdf'

# Initialize yagmail SMTP instance
yag = yagmail.SMTP(email_address, app_password)

# Create Celery application
app = Celery('send_email', broker='redis://localhost:6379/0')

html_content ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Harmonix</title>
</head>
<body>
    <h1>HARMONIX MONTHLY REPORT</h1>
    <p>Check your Monthly Report in this PDF</p>
    <br><br>
    <p><strong>Click this PDF</strong></p>
</body>
</html>

"""

# Define Celery task to send email
@app.task
def send_email():
    yag = yagmail.SMTP('22f3001758@ds.study.iitm.ac.in', 'onypwhekxiwluepa')
    pdf_path = 'MonthlyReport.pdf'

    # Send email using yagmail
    yag.send(
        to='vikash1702palani@gmail.com',
        subject='HARMONIX MONTHLY REPORT',
        attachments=pdf_path,
        contents=html_content,
        headers={'Content-Type': 'text.html'}
    )

# Configure Celery beat schedule
app.conf.beat_schedule = {
    'send-reminder': {
        'task': 'send_html.send_email',
        'schedule': crontab(minute="*")
    },
}

