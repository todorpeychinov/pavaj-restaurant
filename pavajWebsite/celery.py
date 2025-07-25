import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pavajWebsite.settings')

app = Celery('pavajWebsite')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
