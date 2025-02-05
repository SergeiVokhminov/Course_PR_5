from celery import shared_task
from django.utils import timezone

from habittracker.models import Habit
from habittracker.services import send_telegram_message


@shared_task
def send_reminder():
    """Отправляет пользователю в телеграм напоминания о том, в какое время какие привычки необходимо выполнять."""

    habits = Habit.objects.all()
    for habit in habits:
        print(habit)
        if habit.time <= timezone.now().time():
            chat_id = habit.user.tg_id
            print(chat_id)
            message = f"Пора выполнять: {habit.action}"
            send_telegram_message(chat_id, message)
