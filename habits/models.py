from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    habit_option = (
        (True, "Полезная"),
        (False, "Вредная"),
    )

    period_options = (
        (1, "Ежедневно"),
        (7, "Еженедельно"),
        (30, "Ежемесячно"),
    )

    publication_option = (
        (True, "Опубликовано"),
        (False, "Не опубликовано"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    place = models.CharField(
        max_length=300,
        verbose_name="Место",
        help_text="Место в котором необходимо выполнять привычку",
    )
    time = models.TimeField(
        verbose_name="Время",
        help_text="Время, когда надо выполнить привычку",
    )
    action = models.CharField(
        max_length=200,
        verbose_name="Действие",
        help_text="Действие, которое надо сделать",
    )
    duration = models.SmallIntegerField(verbose_name="Продолжительность в минутах")
    periodicity = models.IntegerField(
        default=1, choices=period_options, verbose_name="Периодичность (в днях)"
    )
    sign_of_habit = models.BooleanField(
        default=True, verbose_name="Признак привычки", choices=habit_option
    )
    is_public = models.BooleanField(
        default=False, choices=publication_option, verbose_name="Публичность"
    )
    related = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная с другой привычкой",
        **NULLABLE,
    )
    reward = models.CharField(
        max_length=100,
        verbose_name="Вознаграждение",
        help_text="Чем пользователь может наградить себя после выполнения привычки",
        **NULLABLE,
    )
    is_good = models.BooleanField(default=True, verbose_name="Полезная привычка")

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
        ordering = ["-id"]
