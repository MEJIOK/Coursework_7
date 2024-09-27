from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование модели Habits"""

    def setUp(self):
        """Создание тестовой модели Пользователя (с авторизацией) и Привычки"""
        self.user = User.objects.create(email="test@test.com", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            user=self.user,
            place="Магазин",
            time="18:00:00",
            action="Пойти в магазин за покупками",
            duration=60,
            periodicity=True,
        )

    def test_create_habit(self):
        """Тестирование создания привычки"""
        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "Магазин",
            "time": "18:00:00",
            "action": "Пойти в магазин за покупками",
            "duration": 60,
            "periodicity": True,
        }
        response = self.client.post(url, data=data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("user"), self.user.pk)
        self.assertEqual(data.get("place"), "Магазин")
        self.assertEqual(data.get("time"), "18:00:00")
        self.assertEqual(data.get("action"), "Пойти в магазин за покупками")
        self.assertEqual(data.get("duration"), 60)
        self.assertEqual(data.get("periodicity"), True)

    def test_list_habit(self):
        """Тестирование вывода всех привычек"""
        response = self.client.get(reverse("habits:habits_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """Тестирование просмотра одной привычки"""
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("time"), self.habit.time)
        self.assertEqual(data.get("action"), self.habit.action)
        self.assertEqual(data.get("duration"), self.habit.duration)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)

    def test_update_habit(self):
        """Тестирование изменений привычки"""
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Фитнес-зал",
            "time": "19:00:00",
            "action": "Тренировка в фитнес-зале",
            "duration": 120,
            "periodicity": True,
        }
        response = self.client.put(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), "Фитнес-зал")
        self.assertEqual(data.get("time"), "19:00:00")
        self.assertEqual(data.get("action"), "Тренировка в фитнес-зале")
        self.assertEqual(data.get("duration"), 120)
        self.assertEqual(data.get("periodicity"), True)

    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_public_habit(self):
        """Тестирование вывода публичных привычек"""
        response = self.client.get(reverse("habits:public_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
