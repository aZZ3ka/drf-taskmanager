import random
from celery import shared_task
from django.core.mail import send_mail


@shared_task(name="send_mail")
def send_mail_task(message, user_email):
    send_mail(
        'Notification',
        message,
        'azatashimov1993@gmail.com',
        user_email,
        fail_silently=False,
    )
