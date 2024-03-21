from celery import shared_task
from django.core.mail import send_mail

@shared_task
def enviar_email_reserva(email_destinatario, mensagem):
    send_mail(
        'Confirmação de Reserva',
        mensagem,
        'aramismpb@gmail.com',  # Remetente
        [email_destinatario],
        fail_silently=False,
    )