from django.core.exceptions import ValidationError
from django.db import models

from config.settings import NULLABLE
from users.models import User


class Habit(models.Model):
    PERIODICITY = [
        ('daily', 'Раз в день'),
        ('every_2_days', 'Раз в 2 дня'),
        ('every_3_days', 'Раз в 3 дня'),
        ('weekly', 'Раз в неделю'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habit', **NULLABLE)
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    pleasant = models.BooleanField()
    related = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                related_name='related_habit')
    periodicity = models.CharField(max_length=30, choices=PERIODICITY, default='daily')
    reward = models.CharField(max_length=255, **NULLABLE)
    lead_time = models.DurationField()
    is_public = models.BooleanField(default=False)

    def clean(self):
        if self.related and not self.related.pleasant:
            raise ValidationError("Можно связывать только полезные с приятными привычками")

    def __str__(self):
        return f"{self.user} - {self.action}"
