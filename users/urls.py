from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserCreateApiView,
    UserDeleteApiView,
    UserDetailApiView,
    UserListApiView,
    UserUpdateApiView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateApiView.as_view(), name="register"),
    path("list/", UserListApiView.as_view(), name="user_list"),
    path("detail/<int:pk>/", UserDetailApiView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateApiView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteApiView.as_view(), name="user_delete"),
]
