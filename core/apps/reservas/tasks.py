from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from core.apps.reservas.models import Reserva


@shared_task
def enviar_email_reserva(email_destinatario, mensagem):
    send_mail(
        'Confirmação de Reserva',
        mensagem,
        'aramismpb@gmail.com',  # Remetente
        [email_destinatario],
        fail_silently=False,
    )


@shared_task
def verificar_concluir_reservas():
    reservas_para_concluir = Reserva.objects.filter(data_termino__lt=timezone.now(), status='confirmada')
    for reserva in reservas_para_concluir:
        reserva.status = 'concluida'
        reserva.save()
