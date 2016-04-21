from __future__ import absolute_import
from celery import shared_task

from django.core.mail import send_mail

@shared_task
def send_email_notification(to, subject, text):
    print('sending email...')
    send_mail(subject, text, 'idenxxx@mail.ru', [to], fail_silently=False)
    print('successfully sent email')

@shared_task
def print_num(n):
    print(n)
    from time import sleep
    sleep(2.0)
