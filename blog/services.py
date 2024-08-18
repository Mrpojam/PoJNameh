from django.core.mail import send_mail

from os import environ as env

SENDER_EMAIL_ADDRESS = env.get("SENDER_EMAIL_ADDRESS")
RECEIVER_EMAIL_ADDRESS = env.get("RECEIVER_EMAIL_ADDRESS")

def send_email(text) -> bool:
    success = send_mail(
        "You got a new message!",
        text,
        SENDER_EMAIL_ADDRESS,
        [RECEIVER_EMAIL_ADDRESS],
        fail_silently=False,
    )

    return success