from users.models import User
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    habit_option = (
        (True, 'Полезная'),
        (False, 'Вредная'),
    )
    period = (
        (True, 'Ежедневно'),
        (False, 'Еженедельно'),
    )
    publication_option = (
        (True, 'Опубликовано'),
        (False, 'Не опубликовано'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=300, verbose_name='Место',
                             help_text='Место в котором необходимо выполнять привычку')
    time = models.TimeField(max_length=25, verbose_name='Время', help_text='Время, когда надо выполнить привычку')
    action = models.CharField(max_length=200, verbose_name='Действие', help_text='Действие, которое надо сделать')
    duration = models.SmallIntegerField(verbose_name='Продолжительность в минутах')
    periodicity = models.BooleanField(default=True, choices=period, verbose_name='Периодичность')
    sign_of_habit = models.BooleanField(default=True, verbose_name='Признак привычки', choices=habit_option)
    is_public = models.BooleanField(default=False, choices=publication_option, verbose_name='Публичность')
    related = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная с другой привычкой',
                                **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение',
                              help_text='Чем пользователь может наградить себя после выполнения привычки', **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-id']
