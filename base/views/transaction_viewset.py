from django.conf import settings
from django.db.models import Q

from telegram_django_bot.td_viewset import TelegramViewSet
from telegram_django_bot.telegram_lib_redefinition import InlineKeyboardButtonDJ

from bscscan.models import Transaction
from base.forms import TransactionForm


class TransactionViewSet(TelegramViewSet):
    viewset_name = "Transaction"
    queryset = Transaction.objects.all()
    model_form = TransactionForm
    actions = ["show_elem", "show_list"]

    def show_list(self, page=0, per_page=10, columns=1, *args, **kwargs):
        addresses = self.user.address.all()
        self.queryset = Transaction.objects.filter(
            Q(from_address__in=addresses) | Q(to_address__in=addresses)
        )
        __, (mess, buttons) = super().show_list(page, per_page, columns)
        buttons += [
            [
                InlineKeyboardButtonDJ(
                    text="🔙 Back",
                    callback_data=settings.TELEGRAM_BOT_MAIN_MENU_CALLBACK,
                )
            ],
        ]
        return self.CHAT_ACTION_MESSAGE, (mess, buttons)
