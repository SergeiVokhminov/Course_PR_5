from django.db import models

from users.models import User


class Habit(models.Model):
    """Поля для модели привычки"""

    habit_creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки",
        help_text="Введите создателя привычки",
    )
    place = models.CharField(
        max_length=255,
        verbose_name="Место выполнения привычки",
        help_text="Введите место выполнения привычки",
        blank=True,
        null=True,
    )
    time = models.TimeField(
        verbose_name="Время выполнения привычки",
        help_text="Введите время выполнения привычки",
        null=True,
        blank=True,
    )
    action = models.TextField(
        max_length=255,
        verbose_name="Действие, которое представляет собой привычка",
        help_text="Введите действие привычки",
        blank=True,
        null=True,
    )
    sign_pleasant_habit = models.BooleanField(
        verbose_name="Признак приятной привычки",
        help_text="Установите признак приятной привычки",
        default=False,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        blank=True,
        null=True,
    )
    periodicity = models.IntegerField(
        verbose_name="Периодичность выполнения привычки в днях",
        help_text="Введите периодичность выполнения привычки",
        default=1,
    )
    award = models.CharField(
        max_length=255,
        verbose_name="Вознаграждение за выполнение привычки",
        help_text="Введите вознаграждение за выполнение привычки",
        blank=True,
        null=True,
    )
    duration = models.IntegerField(
        verbose_name="Время на выполнение привычки в секундах",
        help_text="Введите время за которое выполните привычку",
        default=120,
    )
    is_public = models.BooleanField(
        verbose_name="Признак публичности",
        help_text="Введите признак публичности",
        default=True,
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
