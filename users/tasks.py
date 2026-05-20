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


@shared_task
def generate_discount(price):
    discount_price = price - (price * 0.1)
    print(f"Цена со скидкой: {discount_price}")
    return discount_price


@shared_task
def send_welcome_email(email):
    from django.core.mail import send_mail

    send_mail(
        "Регистрация",
        "Спасибо за регистрацию!",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    return "EMAIL SENT"


@shared_task
def clear_old_reviews():
    from product.models import Review

    deleted_reviews = Review.objects.filter(stars=1).delete()

    return f"Deleted: {deleted_reviews}"