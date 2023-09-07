from django.contrib import admin
from bscscan.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("from_address", "to_address")
