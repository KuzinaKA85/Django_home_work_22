from django.db import models


class Article(models.Model):
    title_article = models.CharField(max_length=150, verbose_name="Наименование статьи")
    content_article = models.TextField(verbose_name="Содержание статьи")
    image_article = models.ImageField(
        upload_to="articles/", verbose_name="Изображениe", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_article

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title_article", "created_at", "is_active"]
