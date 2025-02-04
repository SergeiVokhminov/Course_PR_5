from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание пользователя-администратора."""

    def handle(self, *args, **options):
        """Метод создания пользователя-администратора."""
        user = User.objects.create(email="admin@test.ru")
        user.set_password("0admin0")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Пользователь-администратор с электронной почтой {user.email} успешно создан"
            )
        )
