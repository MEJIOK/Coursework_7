# Generated by Django 4.2 on 2024-09-27 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        help_text="Место в котором необходимо выполнять привычку",
                        max_length=300,
                        verbose_name="Место",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        help_text="Время, когда надо выполнить привычку",
                        max_length=25,
                        verbose_name="Время",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        help_text="Действие, которое надо сделать",
                        max_length=200,
                        verbose_name="Действие",
                    ),
                ),
                (
                    "duration",
                    models.SmallIntegerField(
                        verbose_name="Продолжительность в минутах"
                    ),
                ),
                (
                    "periodicity",
                    models.BooleanField(
                        choices=[(True, "Ежедневно"), (False, "Еженедельно")],
                        default=True,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "sign_of_habit",
                    models.BooleanField(
                        choices=[(True, "Полезная"), (False, "Вредная")],
                        default=True,
                        verbose_name="Признак привычки",
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        choices=[(True, "Опубликовано"), (False, "Не опубликовано")],
                        default=False,
                        verbose_name="Публичность",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        help_text="Чем пользователь может наградить себя после выполнения привычки",
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "related",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habits",
                        verbose_name="Связанная с другой привычкой",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
                "ordering": ["-id"],
            },
        ),
    ]
