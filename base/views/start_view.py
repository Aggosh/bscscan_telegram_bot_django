from telegram_django_bot.utils import handler_decor
from telegram_django_bot.telegram_lib_redefinition import InlineKeyboardButtonDJ
from telegram_django_bot.routing import telegram_reverse
from telegram_django_bot.tg_dj_bot import TG_DJ_Bot
from telegram import Update

from base.models import User

from .address_viewset import AddressViewSet
from .transaction_viewset import TransactionViewSet


@handler_decor()
def start(bot: TG_DJ_Bot, update: Update, user: User):
    message = f"Hello, {user.first_name or user.telegram_username or user.id}! I am bot, which track BscScan transactions 🤖"
    buttons = [
        [
            InlineKeyboardButtonDJ(
                text="Address",
                callback_data=AddressViewSet(
                    telegram_reverse("base:AddressViewSet"), user=user
                ).gm_callback_data("show_list"),
            )
        ],
        [
            InlineKeyboardButtonDJ(
                text="Transactions",
                callback_data=TransactionViewSet(
                    telegram_reverse("base:TransactionViewSet"), user=user
                ).gm_callback_data("show_list"),
            )
        ],
    ]

    return bot.edit_or_send(update, message, buttons)
