# utils.py
from django.core.mail import send_mail
from .models import OTP
import random
import string

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

def send_otp(email):
    otp = generate_otp()
    OTP.objects.create(email=email, otp=otp)
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}',
        'suranipal11@gmail.com',
        [email],
        fail_silently=False,
    )
