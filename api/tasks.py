from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber, Content
from decouple import config


@shared_task
def send_newsletter(title, body):
    recipients = [subscriber.email for subscriber in Subscriber.objects.all()]

    send_mail(subject=title,
              message=body,
              from_email=config("EMAIL_HOST_USER"),
              recipient_list=recipients)