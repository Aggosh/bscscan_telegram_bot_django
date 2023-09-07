from bscscan.models import Address
from telegram_django_bot import forms as td_forms


class AddressForm(td_forms.TelegramModelForm):
    form_name = "Address"

    class Meta:
        model = Address
        fields = ["name"]
