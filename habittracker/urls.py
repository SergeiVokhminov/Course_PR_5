from django.urls import path

from habittracker.apps import HabittrackerConfig
from habittracker.views import (
    HabitCreateApiView,
    HabitDeleteApiView,
    HabitDetailApiView,
    HabitListApiView,
    HabitUpdateApiView,
)

app_name = HabittrackerConfig.name

urlpatterns = [
    path("list/", HabitListApiView.as_view(), name="habits_list"),
    path("create/", HabitCreateApiView.as_view(), name="habits_create"),
    path("detail/<int:pk>/", HabitDetailApiView.as_view(), name="habits_detail"),
    path("update/<int:pk>/", HabitUpdateApiView.as_view(), name="habits_update"),
    path("delete/<int:pk>/", HabitDeleteApiView.as_view(), name="habits_delete"),
]
