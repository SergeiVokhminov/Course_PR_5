from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Поля для модели пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=35, verbose_name="Номер телефона", blank=True, null=True
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Город",
        help_text="Введите город",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        upload_to="photo/avatars/",
        verbose_name="Аватар",
        help_text="Загрузите Ваш аватар",
        blank=True,
        null=True,
    )
    tg_id = models.CharField(
        max_length=300,
        verbose_name="ID профиля Telegram",
        help_text="Введите ID Вашего профиля Telegram",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
