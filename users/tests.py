from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тесты."""

    def setUp(self):
        """Подготовка исходных данных для тестов."""

        self.user = User.objects.create(
            email="test@test.com",
            first_name="Test",
            last_name="Test",
            phone_number="+79222222222",
            is_active=True,
            is_superuser=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тест создания нового пользователя."""

        url = reverse("users:register")
        data = {
            "email": "new_test@test.com",
            "password": "12345678Qw",
            "first_name": "Test",
            "last_name": "Test",
            "phone_number": "+79001111111",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_user_list(self):
        """Тест получения списка всех пользователей."""

        url = reverse("users:user_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_user_detail(self):
        """Тест получения информации о пользователе."""

        url = reverse("users:user_detail", args=(self.user.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("email")
        self.assertEqual(result, self.user.email)

    def test_user_update(self):
        """Тест изменения информации о пользователе."""

        url = reverse("users:user_update", args=(self.user.id,))
        data = {"phone_number": "555"}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("phone_number")
        self.assertEqual(result, data.get("phone_number"))

    def test_user_delete(self):
        """Тест удаления пользователя."""

        url = reverse("users:user_delete", args=(self.user.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 0)
