import yagmail
from celery import Celery
from celery.schedules import crontab

# Redis configuration
redis_broker_url = 'redis://localhost:6379/0'
redis_backend_url = 'redis://localhost:6379/0'

# Email configuration
email_address = 'ashwinisp.avd@gmail.com'
app_password = 'tfpazdqysdunlrrr'

# Initialize yagmail SMTP instance
yag = yagmail.SMTP(email_address, app_password)

# Create Celery application
app = Celery('send_email', broker=redis_broker_url, backend=redis_backend_url)

# Optional Celery configuration
app.conf.update(
    result_expires=3600,   # Result expires after 1 hour
    timezone='UTC',        # Celery timezone
    task_serializer='json',  # Task serializer
    accept_content=['json'],  # Accepted content types
)

# Define Celery task to send email
@app.task
def send_email():
    # Send email using yagmail
    yag.send(
        to='ashwinip.bme2020@citchennai.net',
        subject='Harmonix test',
        contents='This is a test mail'
    )

# Configure Celery beat schedule
app.conf.beat_schedule = {
    'send-reminder': {
        'task': 'send_email',  # Task name (defined above)
        'schedule': crontab(minute="*"),  # Execute daily at 20:23 UTC
    },
}
