from django.db import models


# class Category(models.Model):
#     name_category = models.CharField(
#         max_length=150, verbose_name="Наименование категории"
#     )
#     description_category = models.TextField(verbose_name="Описание категории")
#
#     def __str__(self):
#         return self.name_category
#
#     class Meta:
#         verbose_name = "Категория"
#         verbose_name_plural = "Категории"
#         ordering = ["name_category"]


class Article(models.Model):
    title_article = models.CharField(
        max_length=150, verbose_name="Наименование статьи"
    )
    content_article = models.TextField(verbose_name="Содержание статьи")
    image_article = models.ImageField(
        upload_to="articles/", verbose_name="Изображениe", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    views_count = models.IntegerField(verbose_name="Количество просмотров", default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title_article", "created_at", "is_active"]

