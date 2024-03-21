import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')

app = Celery('management')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'verificar-concluir-reservas-diariamente': {
        'task': 'core.apps.reservas.tasks.verificar_concluir_reservas',
        'schedule': crontab(hour='0', minute='2'),  # Executa todos os dias à meia-noite
    },
}