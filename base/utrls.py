from django.urls import re_path

from .views import start, AddressViewSet, TransactionViewSet


urlpatterns = [
    re_path("start", start, name="start"),
    re_path("main_menu", start, name="start"),
    re_path("ad/", AddressViewSet, name="AddressViewSet"),
    re_path("tr/", TransactionViewSet, name="TransactionViewSet"),
]
