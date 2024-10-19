from django.urls import path
from sorsore.views import search

urlpatterns = [
    path("", search, name="crx_search"),
]
