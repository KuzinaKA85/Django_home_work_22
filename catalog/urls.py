from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductUnpublishView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"
    ),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product_delete/<int:pk>/",
        ProductDeleteView.as_view(),
        name="product_confirm_delete",
    ),
    path(
        "product_unpublish/<int:pk>/",
        ProductUnpublishView.as_view(),
        name="product_unpublish",
    ),
]
