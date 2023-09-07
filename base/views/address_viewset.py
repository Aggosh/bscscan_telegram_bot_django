from django.conf import settings

from telegram_django_bot.td_viewset import TelegramViewSet
from telegram_django_bot.telegram_lib_redefinition import InlineKeyboardButtonDJ

from base.forms import AddressForm

from bscscan.models import Address
from bscscan.managers import Parser


class AddressViewSet(TelegramViewSet):
    viewset_name = "Address"
    model_form = AddressForm
    queryset = Address.objects.all()
    actions = ["create", "delete", "show_elem", "show_list"]

    def gm_success_created(self, *args, **kwargs):
        res = super().gm_success_created(*args, **kwargs)
        address = args[0]
        self.user.address.add(address)
        parser = Parser()
        parser.scrap_and_save_transaction(payload={"address": address.name})
        return res

    def delete(self, model_or_pk, is_confirmed=False):
        model = self.get_orm_model(model_or_pk)

        if model:
            if self.deleting_with_confirm and not is_confirmed:
                # just ask for confirmation
                mess, buttons = self.gm_delete_getting_confirmation(model)
            else:
                # real deleting
                self.user.address.remove(model)
                mess, buttons = self.gm_delete_successfully(model)

            return self.CHAT_ACTION_MESSAGE, (mess, buttons)
        else:
            return self.gm_no_elem(model_or_pk)

    def show_list(self, page=0, per_page=10, columns=1, *args, **kwargs):
        self.queryset = self.user.address.all()
        __, (mess, buttons) = super().show_list(page, per_page, columns)

        buttons += [
            [
                InlineKeyboardButtonDJ(
                    text="➕ Add", callback_data=self.gm_callback_data("create")
                )
            ],
            [
                InlineKeyboardButtonDJ(
                    text="🔙 Back",
                    callback_data=settings.TELEGRAM_BOT_MAIN_MENU_CALLBACK,
                )
            ],
        ]
        return self.CHAT_ACTION_MESSAGE, (mess, buttons)
