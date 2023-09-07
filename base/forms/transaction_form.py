from bscscan.models import Transaction
from telegram_django_bot import forms as td_forms


class TransactionForm(td_forms.TelegramModelForm):
    form_name = "Transaction"

    class Meta:
        model = Transaction
        fields = [
            "from_address",
            "to_address",
            "type",
            "block_number",
            "time_stamp",
            "hash",
            "value",
            "gas",
            "txreceipt_status",
            "gas_used",
            "confirmations",
        ]
