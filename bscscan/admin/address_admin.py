from django.contrib import admin
from bscscan.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("name",)
