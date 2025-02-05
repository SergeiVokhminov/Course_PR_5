from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from habittracker.models import Habit
from habittracker.pagination import PageSizePagination
from habittracker.serializers import HabitSerializer
from users.permissions import IsCreated


class HabitCreateApiView(CreateAPIView):
    """Контроллер создания привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        habit = serializer.save(habit_creator=self.request.user)
        habit.save()


class HabitListApiView(ListAPIView):
    """Контроллер списка всех привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = PageSizePagination

    def get_queryset(self):
        return Habit.objects.filter(habit_creator=self.request.user)


class HabitDetailApiView(RetrieveAPIView):
    """Контроллер просмотра информации о привычке."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreated,)
        return super().get_permissions()


class HabitUpdateApiView(UpdateAPIView):
    """Контроллер изменения привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreated,)
        return super().get_permissions()


class HabitDeleteApiView(DestroyAPIView):
    """Контроллер удаления привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreated,)
        return super().get_permissions()
