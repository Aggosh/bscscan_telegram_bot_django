from django.contrib import admin
from base.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_filter = ("first_name", "last_name")
