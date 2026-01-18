from django.contrib import admin

from blogs.models import Article


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "name_category")
#     search_fields = ("name_category", "description_category")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title_article", "content_article", "created_at", "is_active", "views_count")
    list_filter = ("title_article", "created_at", "is_active",)
    search_fields = ("title_article", "content_article")
