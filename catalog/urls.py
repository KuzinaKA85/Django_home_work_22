from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, base, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", base, name="base"),
    path("contacts/", contacts, name="contacts"),
    path("products/<int:pk>/", products_detail, name="products_detail"),
]
