from celery.app import shared_task
from django.core.mail import send_mail


@shared_task
def send_background_mail(subject, message, from_email, recipient_list):
    send_mail(subject, message, from_email, recipient_list)
    print("Email sent successfully")