from django.urls import re_path, include


urlpatterns = [
    re_path("", include(("base.utrls", "base"), namespace="base")),
]
