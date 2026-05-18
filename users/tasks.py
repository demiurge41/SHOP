from celery import shared_task
from django.conf import settings


@shared_task
def add(x, y):
    from time import sleep
    sleep(20)
    print("^"*100)
    return x + y

@shared_task
def send_email(email, code):
    from django.core.mail import send_mail

    send_mail(
        "Добро пожаловать!",
        f"Ваш код: {code}, для регистрации",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return "SENT"

@shared_task
def delete_unactive_users():
    from users.models import CustomUser
    a = CustomUser.objects.filter(is_active=False).delete()
    return f"Deleted {a}"