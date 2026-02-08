from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_category")
    search_fields = ("name_category", "description_category")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name_product",
        "price_product",
        "category_product",
        "is_published",
    )
    list_filter = ("category_product",)
    search_fields = ("name_product", "description_product")
