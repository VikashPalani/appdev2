import yagmail
from celery import Celery
from datetime import timedelta
import redis
from celery.schedules import crontab
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
email_address = 'ashwinisp.avd@gmail.com'
app_password = 'tfpazdqysdunlrrr'

from celery import Celery

# Create Celery application
app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Optional configuration
app.conf.update(
    result_expires=3600,  # Result expires after 1 hour
    timezone='UTC',       # Celery timezone
    task_serializer='json',  # Task serializer
    accept_content=['json'],  # Accepted content types
)

yag = yagmail.SMTP(email_address, app_password)

# app = Celery('send_email', broker='redis://localhost:6379/0')

@app.task
def send_email():
    yag.send(
        to='ashwinip.bme2020@citchennai.net',
        subject='Harmonix test',
        contents='This is a test mail'
    )
app.conf.beat_schedule = {
# Executes every Monday morning at 7:30 a.m.
#crontab(day_of_week="1-5", hour=1, minute=0)
'send-reminder': {
    'task': 'send_mail.send_email',
    'schedule': crontab(minute="*")
  },
}