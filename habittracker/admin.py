from django.contrib import admin

from habittracker.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "habit_creator",
        "place",
        "time",
        "action",
        "sign_pleasant_habit",
        "related_habit",
        "periodicity",
        "award",
        "duration",
        "is_public",
    )
    search_fields = ["habit_creator", "place", "time", "action"]
    list_filter = ["habit_creator", "place", "is_public"]
