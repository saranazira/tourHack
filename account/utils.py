from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    context = {
        'text_detail': 'Спасибо за регистрацию',
        'email': email,
        'domain': 'http://localhost:8000',
        'activation_code': activation_code

    }

    msg_html = render_to_string('email.html', context)
    message = strip_tags(msg_html)
    send_mail(
        'Активация аккаунта',
        message,
        'admin@gmail.com',
        [email],
        html_message=msg_html,
        fail_silently=False
    )