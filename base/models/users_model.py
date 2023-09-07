from django.db import models

from telegram_django_bot.models import TelegramUser

from bscscan.models import Address


class User(TelegramUser):
    address = models.ManyToManyField(Address)
