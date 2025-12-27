from django.db import models


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name='Наименование продукта')
    description_product = models.TextField(verbose_name='Описание продукта')
    image_product = models.ImageField(upload_to='images/', verbose_name='Изображения')
    category_product = models.CharField(max_length=150, verbose_name='Категория продукта')
    price_product = models.FloatField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name_product}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name_product']


class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name='Наименование категории')
    description_category = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.name_category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name_category']