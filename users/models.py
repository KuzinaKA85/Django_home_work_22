from django.contrib.admin.utils import help_text_for_field
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

class User(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone_number = models.CharField(max_length=15,
                                    verbose_name="Телефон",
                                    blank=True, null=True,
                                    help_text="Введите номер телефона"
                                    )
    avatar = models.ImageField(upload_to="users/avatars",
                               verbose_name="Аватар",
                               blank=True,
                               null=True,
                               help_text="Загрузите аватарку")
    country = models.CharField(max_length=50,
                                verbose_name="Страна",
                                blank=True, null=True,
                                help_text="Введите страну проживания"
                               )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

