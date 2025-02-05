from rest_framework.serializers import ModelSerializer

from habittracker.models import Habit
from habittracker.validators import HabitValidator
from users.serializers import UserSerializer


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели привычки."""

    habit_creator = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidator(field="__all__")]
