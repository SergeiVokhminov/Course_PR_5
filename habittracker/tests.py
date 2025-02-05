from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habittracker.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    """Тесты привычки."""

    def setUp(self):
        """Подготовка исходных данных для тестов."""

        self.user = User.objects.create(email="test@test.com")
        self.test_habit = Habit.objects.create(
            habit_creator=self.user,
            place="Test",
            action="Test",
            sign_pleasant_habit=True,
            periodicity=50,
            duration=10,
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_detail(self):
        """Тест получения информации о привычке."""

        url = reverse("habittracker:habits_detail", args=(self.test_habit.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("action")
        self.assertEqual(result, self.test_habit.action)

    def test_habit_create(self):
        """Тест создания новой привычки."""

        url = reverse("habittracker:habits_create")
        data = {
            "habit_creator": self.user.pk,
            "place": "Test",
            "time": "14:00:00",
            "action": "Бег",
            "sign_pleasant_habit": False,
            "related_habit": self.test_habit.id,
            "periodicity": 6,
            "award": "",
            "duration": 100,
            "is_public": True,
        }
        response = self.client.post(url, data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get("time"), "14:00:00")
        self.assertEqual(result.get("periodicity"), 6)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тест изменения привычки."""

        url = reverse("habittracker:habits_update", args=(self.test_habit.id,))
        data = {
            "place": "New_test",
            "action": "New_test",
            "sign_pleasant_habit": True,
            "periodicity": 3,
            "duration": 90,
            "is_public": True,
            "related_habit": "",
            "award": "",
        }
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("place")
        self.assertEqual(result, data.get("place"))

    def test_habit_delete(self):
        """Тест удаления привычки."""

        url = reverse("habittracker:habits_delete", args=(self.test_habit.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тест получения списка привычек."""

        url = reverse("habittracker:habits_list")
        response = self.client.get(url)
        result = {
            "id": self.test_habit.id,
            "action": self.test_habit.action,
            "habit_creator": self.user.id,
        }
        habit_id = response.json().get("results")[0].get("id")
        action = response.json().get("results")[0].get("action")
        creater_id = response.json().get("results")[0].get("habit_creator").get("id")
        result_to_assert = {
            "id": habit_id,
            "action": action,
            "habit_creator": creater_id,
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_to_assert, result)

    def test_habit_create_wrong(self):
        """Тест получения сообщения о неверной длительности при создании привычки."""
        url = reverse("habittracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "sign_pleasant_habit": False,
            "periodicity": 3,
            "duration": 200,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "award": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Время выполнения привычки не может превышать 120 секунд."],
        )

    def test_habit_create_wrong_periodicity(self):
        """Тест получения сообщения о неверной периодичности при создании привычки."""
        url = reverse("habittracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "sign_pleasant_habit": False,
            "periodicity": 10,
            "duration": 100,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "award": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            [
                "Периодичность выполнения привычки не может быть реже чем один раз в неделю."
            ],
        )

    def test_habit_create_reward_related_habit(self):
        """Тест получения сообщения об одновременно выборе награды и связанной привычки при создании."""
        url = reverse("habittracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "sign_pleasant_habit": False,
            "periodicity": 2,
            "duration": 100,
            "is_public": True,
            "related_habit": self.test_habit.id,
            "award": "Test",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Нельзя выбирать связанную привычку и вознаграждение одновременно."],
        )

    def test_habit_create_award_for_pleasant_habit(self):
        """Тест получения сообщения о неверном выборе награды
        и связанной привычки при создании приятной привычки."""
        url = reverse("habittracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "sign_pleasant_habit": True,
            "periodicity": 2,
            "duration": 100,
            "is_public": True,
            "related_habit": "",
            "award": "Test",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            [
                "Нельзя выбирать связанную привычку или вознаграждение для приятной привычки."
            ],
        )
