from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    chat_id = models.CharField(max_length=30, **NULLABLE)

    def __str__(self):
        return self.chat_id
