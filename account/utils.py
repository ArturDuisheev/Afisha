from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError
import random
import string


def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def send_confirmation_code_email(email, code):
    try:
        send_mail(
            subject='Код подтверждения',
            message=f'Ваш код подтверждения: {code}',
            from_email='myworkingartur@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        raise ValidationError({'detail': 'Ошибка при отправке кода подтверждения на почту'})
