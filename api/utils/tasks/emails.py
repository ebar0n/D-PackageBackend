# -*- coding: utf-8 -*-
from api.celery import app
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template


@app.task(name='send_mail')
def send_mail(recipient_list, subject, template_name, data):
    """
    Just send an email

    :param recipient_list: list
    :param subject: str
    :param template_name: str
    :param data: dict
    :return:

    """

    html_content = get_template('emails/' + template_name).render(Context(data))
    msg = EmailMultiAlternatives(subject, '', settings.DEFAULT_FROM_EMAIL, recipient_list)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
