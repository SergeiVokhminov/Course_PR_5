from rest_framework.permissions import BasePermission


class IsCreated(BasePermission):
    """Проверка на создателя объекта."""

    def has_object_permission(self, request, view, obj):
        return obj.habit_creator == request.user
